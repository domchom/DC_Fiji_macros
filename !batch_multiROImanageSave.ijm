// !batch_multiROImanageSave.ijm
// Duplicates each ROI in the ROI Manager across the full stack (all channels,
// z and frames) of the active image and saves each one as a TIFF.
// Existing files are skipped, so the macro can be re-run after adding ROIs.
//
// Usage:  make the hyperstack active, load ROIs into the ROI Manager,
//         edit the parameters below, run.
// Output: <group>-<roi index>.tif

// ===== PARAMETERS =====
output_folder_path = "/Volumes/DOM_SEVEN/371DCE_260624_embryos-fix-Ect2-WTvWA/diseect_scope/frames1to134_single-cells/"; // "" = ask
group = "WA";   // filename prefix, e.g. the condition
// ======================

n = roiManager("count");
if (n == 0) exit("No ROIs in the ROI Manager.");
output_folder_path = prepareOutputFolder(output_folder_path);

setBatchMode(true);
srcID = getImageID();

for (i = 0; i < n; i++) {
	outPath = output_folder_path + group + "-" + i + ".tif";
	if (File.exists(outPath)) {
		print("Skipping (already exists): " + outPath);
		continue;
	}
	selectImage(srcID);
	roiManager("select", i);
	run("Duplicate...", "title=__roi duplicate");
	saveAs("Tiff", outPath);
	close();
}

selectImage(srcID);
setBatchMode(false);
print("Done. Saved crops to " + output_folder_path);


// ===== HELPERS =====

// Returns a usable output folder: asks if empty, adds a trailing slash, and
// creates it (including any missing parent folders).
function prepareOutputFolder(path) {
	if (path == "") path = getDirectory("Choose an output folder");
	if (!endsWith(path, "/")) path = path + "/";
	parts = split(path, "/");
	dir = "";
	if (startsWith(path, "/")) dir = "/";
	for (i = 0; i < parts.length; i++) {
		dir = dir + parts[i] + "/";
		if (!File.exists(dir)) File.makeDirectory(dir);
	}
	return path;
}
