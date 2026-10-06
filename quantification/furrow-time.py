#!/usr/bin/env python3
"""
Batch furrow-timing analysis for cleavage-stage embryo crops.

For every .tif stack in a folder, this:
  1. auto-locates the furrow (the region that darkens most over time),
  2. measures localized furrow DEPTH per frame,
  3. detects furrow START (sustained rise) and END,
  4. flags low-quality cells (weak/noisy furrow) instead of guessing,
  5. saves a depth-curve plot per cell and one combined results CSV.

Run:
    python furrow_timing.py

Requirements:
    pip install tifffile numpy matplotlib
"""

import os
import glob
import csv
import numpy as np
import tifffile
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ===== EDIT THESE =====
IN_DIR        = "/Volumes/DOM_SEVEN/365DCE_260518_embryo-dissect/1st-div-control-cells"
OUT_CSV       = os.path.join(IN_DIR, "!furrow_timing.csv")
PLOT_DIR      = os.path.join(IN_DIR, "!furrow_plots")
INTERVAL_S    = 20.0          # seconds per frame
ENDPOINT      = "90pct"       # "90pct" (start->90% max depth) or "peak" (start->max depth)
EXCLUDE_BAD   = False         # False: keep bad cells in CSV with qc_fail flag. True: drop them.

# detection / QC params (sensible defaults; tune if needed)
BASELINE_FRAMES = 10          # frames used to define pre-furrow baseline
START_THRESH    = 0.15        # normalized depth crossing that defines onset
SMOOTH_WIN      = 5           # frame smoothing window for depth curve
DISK_RADIUS     = 95          # px; central disk isolating cell interior from grid bg
FURROW_BOX      = 12          # px half-width of box measured at the furrow
MIN_DEPTH_CONTRAST = 18.0     # min (baseline-peak) intensity drop, in gray levels, to pass QC
MIN_MONOTONICITY   = 0.60     # fraction of frames onset->peak that are non-decreasing, to pass QC
# ======================


def smooth(x, w):
    if w <= 1:
        return x
    k = np.ones(w) / w
    return np.convolve(x, k, mode="same")


def analyze_stack(arr):
    """arr: (T, Y, X) grayscale float. Returns dict of results."""
    T, Y, X = arr.shape
    base = arr[:BASELINE_FRAMES].mean(0)

    # locate furrow = pixels that darken most relative to baseline at any timepoint
    drop_stack = base[None, :, :] - arr
    maxdrop = drop_stack.max(0)

    # restrict to central disk so bright grid background isn't picked
    yy, xx = np.mgrid[0:Y, 0:X]
    cy, cx = Y // 2, X // 2
    disk = (yy - cy) ** 2 + (xx - cx) ** 2 <= DISK_RADIUS ** 2
    maxdrop_in = np.where(disk, maxdrop, -np.inf)

    mask = maxdrop_in > np.percentile(maxdrop_in[disk], 99.5)
    ys, xs = np.where(mask)
    fy, fx = int(ys.mean()), int(xs.mean())

    # measure mean intensity in a box at the furrow over time
    r = FURROW_BOX
    y0, y1 = max(0, fy - r), min(Y, fy + r)
    x0, x1 = max(0, fx - r), min(X, fx + r)
    box = arr[:, y0:y1, x0:x1].mean(axis=(1, 2))

    base_box = box[:BASELINE_FRAMES].mean()
    depth_raw = base_box - box                 # gray levels darker than baseline
    contrast = float(depth_raw.max())          # absolute depth in gray levels (for QC)

    depth = depth_raw / depth_raw.max() if depth_raw.max() > 0 else depth_raw
    ds = smooth(depth, SMOOTH_WIN)

    peak = int(np.argmax(ds))
    # onset: start of the SUSTAINED rise that leads to the peak, so an early
    # texture transient (bump-and-fall) can't be mistaken for furrow start.
    # Walk back from the peak to the last frame where depth was below START_THRESH
    # AND stayed below it without first dipping back down afterwards.
    start = peak
    for i in range(peak, 0, -1):
        if ds[i] < START_THRESH:
            start = i
            break
    # refine: ensure no deeper dip between this start and the peak (i.e. the rise
    # from `start` to `peak` is the final, monotonic-ish climb, not a recovery
    # after a transient). If a lower point exists later, move start to it.
    if peak > start:
        local_min_rel = int(np.argmin(ds[start:peak + 1]))
        start = start + local_min_rel

    if ENDPOINT == "peak":
        end = peak
    else:  # 90pct
        target = 0.90 * ds.max()
        e = np.where(ds[:peak + 1] >= target)[0]
        end = int(e[0]) if len(e) else peak

    # QC: monotonicity of onset->peak segment
    seg = ds[start:peak + 1]
    if len(seg) > 1:
        diffs = np.diff(seg)
        monotonicity = float((diffs >= -1e-9).mean())
    else:
        monotonicity = 0.0

    qc_reasons = []
    if contrast < MIN_DEPTH_CONTRAST:
        qc_reasons.append(f"weak_contrast({contrast:.1f}<{MIN_DEPTH_CONTRAST})")
    if monotonicity < MIN_MONOTONICITY:
        qc_reasons.append(f"noisy_rise({monotonicity:.2f}<{MIN_MONOTONICITY})")
    qc_pass = len(qc_reasons) == 0

    return {
        "furrow_y": fy, "furrow_x": fx,
        "start_frame": start, "end_frame": end, "peak_frame": peak,
        "duration_frames": end - start,
        "duration_min": round((end - start) * INTERVAL_S / 60.0, 2),
        "depth_contrast": round(contrast, 1),
        "monotonicity": round(monotonicity, 2),
        "qc_pass": qc_pass,
        "qc_reason": ";".join(qc_reasons) if qc_reasons else "",
        "_depth": depth, "_ds": ds,
    }


def main():
    os.makedirs(PLOT_DIR, exist_ok=True)
    files = sorted(glob.glob(os.path.join(IN_DIR, "*.tif")) +
                   glob.glob(os.path.join(IN_DIR, "*.tiff")))
    if not files:
        raise SystemExit(f"No .tif files found in {IN_DIR}")

    rows = []
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        arr = tifffile.imread(f).astype(float)
        if arr.ndim == 4:               # (T,C,Y,X) -> grayscale
            arr = arr.mean(axis=1)
        if arr.ndim != 3:
            print(f"  SKIP {name}: unexpected shape {arr.shape}")
            continue

        res = analyze_stack(arr)

        if EXCLUDE_BAD and not res["qc_pass"]:
            print(f"  EXCLUDE {name}: {res['qc_reason']}")
            continue

        rows.append((name, res))
        flag = "OK" if res["qc_pass"] else f"QC_FAIL [{res['qc_reason']}]"
        print(f"  {name}: start {res['start_frame']}  end {res['end_frame']}  "
              f"dur {res['duration_min']} min  {flag}")

        # plot
        t = np.arange(len(res["_depth"])) * INTERVAL_S / 60.0
        plt.figure(figsize=(6, 3.2))
        plt.plot(t, res["_depth"], lw=0.8, alpha=0.5, label="depth")
        plt.plot(t, res["_ds"], lw=1.8, label="smoothed")
        plt.axvline(res["start_frame"] * INTERVAL_S / 60.0, color="g", ls="--", label="start")
        plt.axvline(res["end_frame"] * INTERVAL_S / 60.0, color="r", ls="--", label="end")
        plt.title(f"{name}  ({'OK' if res['qc_pass'] else 'QC_FAIL'})")
        plt.xlabel("time (min)"); plt.ylabel("norm. furrow depth")
        plt.legend(fontsize=7); plt.tight_layout()
        plt.savefig(os.path.join(PLOT_DIR, f"{name}.png"), dpi=110)
        plt.close()

    # CSV
    cols = ["cell", "start_frame", "end_frame", "peak_frame",
            "duration_frames", "duration_min", "depth_contrast",
            "monotonicity", "qc_pass", "qc_reason", "furrow_y", "furrow_x"]
    with open(OUT_CSV, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for name, r in rows:
            w.writerow([name, r["start_frame"], r["end_frame"], r["peak_frame"],
                        r["duration_frames"], r["duration_min"], r["depth_contrast"],
                        r["monotonicity"], r["qc_pass"], r["qc_reason"],
                        r["furrow_y"], r["furrow_x"]])

    npass = sum(1 for _, r in rows if r["qc_pass"])
    print(f"\nWrote {OUT_CSV}")
    print(f"  {len(rows)} cells analyzed, {npass} passed QC, {len(rows)-npass} flagged")
    print(f"  plots in {PLOT_DIR}")
    durs = [r["duration_min"] for _, r in rows if r["qc_pass"]]
    if durs:
        print(f"  QC-pass duration: mean {np.mean(durs):.2f} min, "
              f"median {np.median(durs):.2f}, n={len(durs)}")


if __name__ == "__main__":
    main()