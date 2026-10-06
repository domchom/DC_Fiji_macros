#!/usr/bin/env python3
"""Create difference movies from multi-channel time-lapse TIFFs.

For every channel, subtract frame t from frame t + DIFFERENCE_NUMBER and
write the result out as a multi-channel TIFF.
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import tifffile

DIFFERENCE_NUMBER = 12
INPUT_FOLDER = Path(
    "/Volumes/DOM_SEVEN/387_389_combined/raw_dbs"
)
OUTPUT_FOLDER = Path(
    "/Volumes/DOM_SEVEN/387_389_combined/raw_dbs_diff"
)
EXTENSIONS = (".tif", ".tiff")


def load_stack(path):
    """Return the image as a TCYX array plus its ImageJ metadata."""
    with tifffile.TiffFile(path) as tif:
        series = tif.series[0]
        data = series.asarray()
        axes = series.axes
        ij_meta = dict(tif.imagej_metadata or {})

    for axis in list(axes):
        if axis not in "TZCYX":
            idx = axes.index(axis)
            data = np.take(data, 0, axis=idx)
            axes = axes[:idx] + axes[idx + 1:]

    if "T" not in axes and "Z" in axes:
        axes = axes.replace("Z", "T")
    elif "Z" in axes:
        idx = axes.index("Z")
        if data.shape[idx] != 1:
            raise ValueError(f"unsupported Z dimension of size {data.shape[idx]}")
        data = np.take(data, 0, axis=idx)
        axes = axes.replace("Z", "")

    if "Y" not in axes or "X" not in axes:
        raise ValueError(f"missing spatial axes (found {axes})")

    if "T" not in axes:
        data = data[np.newaxis]
        axes = "T" + axes
    if "C" not in axes:
        idx = axes.index("T") + 1
        data = np.expand_dims(data, axis=idx)
        axes = axes[:idx] + "C" + axes[idx:]

    order = [axes.index(a) for a in "TCYX"]
    return np.transpose(data, order), ij_meta


def difference_movie(stack, difference_number):
    """stack is TCYX; returns frame[t + n] - frame[t].

    Float inputs stay float32. Integer inputs are subtracted in a wider
    signed type and returned as int16 so negative values survive.
    """
    frames = stack.shape[0]
    if frames <= difference_number:
        raise ValueError(f"stack has {frames} frames, needs more than "
                         f"{difference_number}")

    if np.issubdtype(stack.dtype, np.floating):
        work = np.float32
        first = stack[difference_number:].astype(work)
        last = stack[:frames - difference_number].astype(work)
        return first - last

    first = stack[difference_number:].astype(np.int32)
    last = stack[:frames - difference_number].astype(np.int32)
    return np.clip(first - last, -32768, 32767).astype(np.int16)


def process_file(path, output_folder, difference_number):
    stack, ij_meta = load_stack(path)
    diff = difference_movie(stack, difference_number)

    metadata = {"axes": "TCYX", "mode": "composite"}
    for key in ("finterval", "spacing", "unit", "fps"):
        if key in ij_meta:
            metadata[key] = ij_meta[key]

    out_path = Path(output_folder) / f"{path.stem}_diff{difference_number}.tif"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tifffile.imwrite(out_path, diff, imagej=True, metadata=metadata,
                     photometric="minisblack")
    return out_path, diff


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--input", type=Path, default=INPUT_FOLDER,
                        help="TIFF file or folder of TIFFs to process")
    parser.add_argument("-o", "--output", type=Path, default=OUTPUT_FOLDER,
                        help="folder for the difference movies")
    parser.add_argument("-n", "--difference-number", type=int,
                        default=DIFFERENCE_NUMBER,
                        help="frame interval used for the subtraction")
    args = parser.parse_args()

    if args.input.is_dir():
        files = sorted(p for p in args.input.iterdir()
                       if p.suffix.lower() in EXTENSIONS)
    elif args.input.is_file():
        files = [args.input]
    else:
        print(f"Input path does not exist: {args.input}", file=sys.stderr)
        return 1

    if not files:
        print(f"No TIFF files found in {args.input}", file=sys.stderr)
        return 1

    for path in files:
        try:
            out_path, diff = process_file(path, args.output,
                                          args.difference_number)
        except Exception as exc:
            print(f"{path.name}: {exc}", file=sys.stderr)
        else:
            print(f"{path.name} -> {out_path.name}  "
                  f"{diff.shape} {diff.dtype} "
                  f"min={diff.min():.4g} max={diff.max():.4g}")
    return 0


if __name__ == "__main__":
    sys.exit(main())