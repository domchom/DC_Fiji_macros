import re
import numpy as np
import tifffile
from pathlib import Path
from PIL import Image
from tqdm import tqdm

folder = Path('/Users/domchom/Desktop/402DCE')

TARGET_HEIGHT = 1080    # downsample so frames are this many pixels tall (1080p)


def natkey(p):
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r'(\d+)', p.name)]


def load_frame(f):
    """Load a JPEG, downsample to TARGET_HEIGHT, and split RGB -> (C, Y, X)."""
    img = Image.open(f).convert('RGB')
    w, h = img.size

    if h > TARGET_HEIGHT:
        img = img.resize(
            (round(w * TARGET_HEIGHT / h), TARGET_HEIGHT),
            Image.LANCZOS
        )

    return np.moveaxis(np.asarray(img), -1, 0)


# Stage 1: scan folder for JPEGs
print('[1/3] Scanning for JPEGs...')

files = sorted(
    (
        p for p in folder.iterdir()
        if p.suffix.lower() in ('.jpg', '.jpeg')
        and not p.name.startswith('._')   # Ignore macOS metadata files
    ),
    key=natkey,
)

if not files:
    raise SystemExit(f'No JPEGs found in {folder}')

print(f'Found {len(files)} JPEG frames.')


# Stage 2: measure total size from the first frame
# (avoids loading everything into RAM)
print('[2/3] Measuring dimensions...')

first = load_frame(files[0])  # (C, Y, X)
size_gb = first.nbytes * len(files) / 1e9


# Stage 3: stream each JPEG straight to the TIFF
# (one frame in memory at a time)
out = folder.parent / 'movie.tif'


def planes():
    """Yield one (Y, X) plane per channel, per frame."""
    for f in tqdm(files, desc='[3/3] Writing TIFF', unit='frame'):
        for plane in load_frame(f):
            yield plane


with tifffile.TiffWriter(
    out,
    imagej=size_gb < 3.9,
    bigtiff=size_gb >= 3.9
) as tif:

    tif.write(
        planes(),
        shape=(len(files), first.shape[0], first.shape[1], first.shape[2]),
        dtype=first.dtype,
        photometric='minisblack',
        metadata={'axes': 'TCYX', 'mode': 'composite'}
    )


print(
    f'Wrote {out} — '
    f'{len(files)} frames @ {first.shape[2]}x{first.shape[1]}, '
    f'{first.shape[0]} channels, '
    f'{size_gb:.1f} GB'
)