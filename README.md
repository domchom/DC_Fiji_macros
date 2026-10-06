# DC Fiji Macros

ImageJ/Fiji macros (`.ijm`) for batch-processing microscopy movies, plus a few
Python helpers. Files starting with `!` are the ones used most often.

## How the macros work

Every macro follows the same layout:

```
// <name>.ijm
// What it does, how to use it, what it saves.

// ===== PARAMETERS =====
output_folder_path  = "/path/to/output/";   // "" = ask with a folder picker
channels_to_process = "all";                // "all" or a list, e.g. "1,3"
...
// ======================

<main loop>

// ===== HELPERS =====
<shared helper functions>
```

To run a macro:

1. Open the images in Fiji.
2. Open the macro (Plugins > Macros > Edit...) and edit the `PARAMETERS` block.
3. Click **Run**.

The macros follow these conventions:

- **Batch over open images.** Most macros process every open image in turn,
  save the result, and close it. Unless noted, the original files on disk are
  never modified.
- **Output folder.** `output_folder_path` can be a hardcoded path. If you set it
  to `""`, the macro asks for a folder. Missing folders, including missing
  parent folders, are created automatically.
- **Output names.** Results are saved as `<original name><suffix>.tif`. Each
  macro lists its suffix below.
- **Any number of channels.** Single- and multi-channel images both work.
  `channels_to_process` picks which channels a step applies to. Unselected
  channels are passed through unchanged, except where noted. Channel
  colours (LUTs) are kept.
- **Clean-up.** Each macro closes only the windows it created and the image it
  just processed. Other open images stay queued.
- **In-place macros.** The macros marked *in place* overwrite the original files
  with **File > Save** instead of writing to an output folder.

## Processing

| Macro | What it does | Key parameters | Output |
|---|---|---|---|
| `!Automated_3dRegSaveAndClose.ijm` | Registers multi-channel time-lapses with PoorMan3DReg (translation), using all channels together. Then applies LUTs and auto-contrast. | `luts` | `_reg.tif` |
| `!Automated_minCropSaveClose.ijm` | Crops registered movies to the area with signal in every frame. This trims the zero-filled borders left by registration. | — | `_crop.tif` |
| `!Automated_DiffMC.ijm` | Difference movie: frame *t+N* minus frame *t* for each selected channel. Negative values are clipped to 0 and the result is saved as 16-bit. Unselected channels are dropped. | `difference_number`, `channels_to_process` | `_diff<N>.tif` |
| `!Automated_remove_static.ijm` | Finds static pixels (intensity range over time ≤ threshold, e.g. hot pixels or debris) and replaces them with the local median in every frame. | `range_threshold`, `median_radius`, `channels_to_process` | `_static-removed.tif` |
| `!batch_BleachCorrect.ijm` | Bleach correction (Exponential Fit or Histogram Matching) on selected channels. With Exponential Fit, channels that don't decay are skipped. | `correction_type`, `channels_to_process` | `_bleach_corr.tif` |
| `!batch_rollingFrame_adj.ijm` | Removes slow background: `original − scaling_factor × running average`. | `rolling_frames`, `scaling_factor`, `channels_to_process` | `_rolling_corr.tif` |
| `!batch_DivbySum.ijm` | Divides each selected channel by its own sum projection over time. Output is 32-bit. | `channels_to_process` | `_div-by-sum.tif` |
| `batch_GaussianBlur.ijm` | Gaussian blur on selected channels. | `sigma`, `channels_to_process` | `_blur<sigma>.tif` |
| `batch_AddNoise.ijm` | Adds Gaussian noise to selected channels, e.g. for testing analysis robustness. | `noise_level`, `channels_to_process` | `_noise<level>.tif` |
| `batch_CumulativeMax.ijm` | Cumulative max projection: slice *i* = max of slices 1..*i*. | `channels_to_process` | `_cumMax.tif` |
| `batch_FFTcorrect.ijm` | **Interactive.** For each selected channel, shows the FFT. You select the contaminating frequencies (e.g. stripe peaks), and they are filtered out of the whole stack. | `mask_blur_sigma`, `channels_to_process` | `_FFT_correct.tif` |

## Channels

| Macro | What it does | Key parameters | Output |
|---|---|---|---|
| `batch_ArrangeChannels.ijm` | Reorders, swaps or removes channels. `"21"` swaps a 2-channel image, `"213"` swaps 1 and 2 in a 3-channel image, and `"12"` drops channel 3. | `new_order` | `_ch<order>.tif` |
| `batch_ChannelMath.ijm` | `channel_a − channel_b` or `channel_a ÷ channel_b`. The result is added as the last channel, and the inputs are dropped unless `keep_inputs = true`. Divide is done in 32-bit. | `operation`, `channel_a`, `channel_b`, `keep_inputs` | `_C1-C2.tif` / `_C1divC2.tif` |
| `batch_FlipCh.ijm` | Flips selected channels horizontally or vertically, e.g. to fix a mirrored camera. | `direction`, `channels_to_process` | `_flipped.tif` |
| `batch_RotateCh.ijm` | Rotates selected channels 90° and crops all channels to a matching square. | `direction`, `channels_to_process` | `_rotated.tif` |

## Stacks, frames and properties

| Macro | What it does | Key parameters | Output |
|---|---|---|---|
| `batch_ReorderHyperstack.ijm` | Swaps two hyperstack dimensions (`z-t`, `c-z`, `c-t`), e.g. when z and t were mixed up. Optionally max-projects over z afterwards. | `swap`, `max_project` | `_reordered.tif` / `_MIP.tif` |
| `batch_TrimFrames.ijm` | Keeps frames `first_frame`..`last_frame` (all channels and z). | `first_frame`, `last_frame` | `_frames<a>-<b>.tif` |
| `!batch_ChangeFrameInterval.ijm` | Sets the frame interval, and the pixel size if `pixel_size > 0`. **In place.** | `frame_interval`, `pixel_size` | overwrites original |
| `!batch_ChangeLUTs.ijm` | Applies per-channel LUTs and resets display ranges. Single-channel images get Grays. **In place.** | `luts` | overwrites original |
| `batch_ChangeAnimationSpeed.ijm` | Sets playback speed (fps). **In place.** | `animation_speed` | overwrites original |
| `batch_ChangeImageType.ijm` | Converts to 8-, 16- or 32-bit. **In place.** | `image_type` | overwrites original |

## Interactive ROI tools

These play each movie and wait for you to draw a selection, then click **OK**.

| Macro | What it does | Output |
|---|---|---|
| `!batch_SelectCrop.ijm` | Crops all channels and frames to your selection. Images with no selection are skipped. | `_crop.tif` |
| `batch_SelectCropSingleframe.ijm` | Saves the current frame (all channels) cropped to your selection. | `_crop_one_frame.tif` |
| `batch_SelectRoiKymo.ijm` | Draw a line. A kymograph is made along it (Reslice). | `_kymo.tif` |
| `!batch_multiROImanageSave.ijm` | Not a loop over open images: it uses the **active** image and the ROI Manager. Saves each ROI as its own full stack. Existing files are skipped, so it can be re-run. | `<group>-<index>.tif` |

## Export

| Macro | What it does | Key parameters |
|---|---|---|
| `!batch_Export.ijm` | Saves each image as TIFF, JPEG or AVI. It can save the whole image (`save_merged`) and/or chosen channels as separate grayscale files (`save_channels`). JPEG saves the current frame only. | `format`, `save_merged`, `save_channels`, `gray_channels`, `suffix` |

Output names: `<name><suffix>.<ext>` for the whole image and `<name><suffix>_Ch<c>.<ext>` for each channel.

## Quantification (`quantification/`)

| File | What it does |
|---|---|
| `batch_calculate_wave_speed.ijm` | **Interactive.** On kymographs, add lines along wave fronts to the ROI Manager. Speed = \|Δx · pixel width\| / \|Δy · frame interval\|. Results go to a *Wave speeds* table, and the per-image mean goes to the Log. Pixel size and frame interval must be set correctly. |
| `batch_OptoQuant.ijm` | **Interactive.** Draw one ROI. For every open movie and channel, it reports mean(post_frame) / mean(pre_frame) in an *Opto quant* table. |
| `furrow-time.py` | Python. Automatic furrow-timing analysis for single-cell embryo crops. It finds the furrow, measures its depth over time, detects start and end, and saves plots plus a CSV. |
| `!z_Batch GLCM script.py` | Fiji script (Jython). Batch GLCM texture features for a folder of images. |
| `!z_Haralick Corr Diff.py` | Fiji script (Jython). Haralick correlation and difference features for one image. |
| `!calc_pos-res.ipynb` | Notebook. Finds positively charged (K/R/H) regions in protein sequences. |

## Embryo analysis (`embryo-analysis0stuff/`)

| File | What it does |
|---|---|
| `dissection-scope-div-time-blind.ijm` | Blind furrow timing. Shows single-cell TIFFs (e.g. from `!batch_multiROImanageSave`) in random order with their identity hidden. You enter start and end frames, which are saved to `blind_key.csv` and `furrow_scores.csv`. It can resume where you left off. |
| `analyze_times.py` | Python. Joins `blind_key.csv` and `furrow_scores.csv` and drops excluded cells. Writes `furrow_unblinded.csv` (one row per cell) and `furrow_group_summary.csv` (n, mean, median, SD, SEM, min and max per group). |
| `jpeg-folder-to-tif.py` | Python. Turns a folder of JPEG frames into a downsampled TIFF stack. |
| `mov-to-tiff.py` | Python. Turns a `.mov` into an ImageJ-compatible TCYX TIFF with the frame interval in its metadata. |

## Other

| File | What it does |
|---|---|
| `extract-image-times.ipynb` | Notebook. Pulls acquisition dates and times from PrairieView (PVScan) XML files into a CSV. |

## Plugin requirements

| Plugin | Used by |
|---|---|
| PoorMan3DReg | `!Automated_3dRegSaveAndClose.ijm` |
| Bleach Correction (CorrectBleach) | `!batch_BleachCorrect.ijm` |
| Running ZProjector2 | `!batch_rollingFrame_adj.ijm` |
