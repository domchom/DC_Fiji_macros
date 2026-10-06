#!/usr/bin/env python3
"""
Convert a .mov movie into a 4D TIFF stack (T, C, Y, X), ImageJ/Fiji compatible.

Edit the INPUT, OUTPUT, INTERVAL, and COMPRESS variables below, then run:
    python mov_to_4d_tiff.py

Requirements:
    pip install imageio imageio-ffmpeg av tifffile numpy

Frame interval (seconds) is written into the TIFF metadata so Fiji shows real
time on the T axis. At 20 s/frame: time(min) = frame_index / 3.
"""

import numpy as np
import imageio.v3 as iio
import tifffile

# ----- edit these -----
INPUT = "/Volumes/DOM_SEVEN/371DCE_260624_embryos-fix-Ect2-WTvWA/371DCE.mov"
OUTPUT = "/Volumes/DOM_SEVEN/371DCE_260624_embryos-fix-Ect2-WTvWA/371DCE_dissection-scope.tif"
INTERVAL = 20.0    # acquisition interval, seconds per frame
COMPRESS = False   # True for a smaller deflate-compressed stack
# ----------------------


def main():
    # Read every frame -> (T, Y, X, C)
    frames = [f for f in iio.imiter(INPUT, plugin="FFMPEG")]
    stack = np.stack(frames, axis=0)
    t, y, x, c = stack.shape

    # ImageJ hyperstack axis order: T, C, Y, X
    stack_ij = np.moveaxis(stack, 3, 1)  # (T, C, Y, X)

    kwargs = dict(
        imagej=True,
        metadata={"axes": "TCYX", "finterval": INTERVAL, "unit": "pixel"},
    )
    if COMPRESS:
        kwargs["compression"] = "deflate"

    tifffile.imwrite(OUTPUT, stack_ij, **kwargs)

    print(f"wrote {OUTPUT}")
    print(f"  T={t}  C={c}  Y={y}  X={x}")
    print(f"  interval {INTERVAL} s/frame -> time(min) = frame / {60/INTERVAL:g}")


if __name__ == "__main__":
    main()