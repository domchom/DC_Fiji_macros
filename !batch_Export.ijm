// !batch_Export.ijm
// Exports every open image as TIFF, JPEG or AVI: the whole (merged) image and/or
// the selected channels as separate grayscale files.
// JPEG saves the current frame only; AVI saves the whole movie.
//
// Usage:  open the images, edit the parameters below, run.
// Output: <name><suffix>.<ext>            when save_merged = true
//         <name><suffix>_Ch<c>.<ext>      for each channel in save_channels

// ===== PARAMETERS =====
output_folder_path = "/Volumes/DOM_EIGHT/pos-feedback-paper-data/260824-figureFiles/Fig5_GEF4A/"; // "" = ask
format        = "AVI";    // "Tiff", "Jpeg" or "AVI"
save_merged   = true;     // save the whole image as-is
save_channels = "none";   // "none", "all" or a list, e.g. "1,3"
gray_channels = true;     // single-channel exports use Grays + auto-contrast
suffix        = "";       // appended to every file name, e.g. "_kymo"
// ======================

if      (format == "Tiff") ext = ".tif";
else if (format == "Jpeg") ext = ".jpg";
else if (format == "AVI")  ext = ".avi";
else exit("Unknown format: " + format);

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	inputID = getImageID();
	baseName = getBaseName(getTitle());
	baseName = baseName + suffix;

	if (save_merged) {
		saveAs(format, output_folder_path + baseName + ext);
	}

	if (save_channels != "none") {
		selectImage(inputID);
		nCh = splitChannels();
		for (c = 1; c <= nCh; c++) {
			if (!isChannelSelected(save_channels, c)) continue;
			selectWindow("__ch" + c);
			if (gray_channels) {
				run("Grays");
				run("Enhance Contrast", "saturated=0.35");
			}
			saveAs(format, output_folder_path + baseName + "_Ch" + c + ext);
		}
	}
	closeAllExcept(otherIDs);
}


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

// Returns the title without its file extension.
function getBaseName(title) {
	dot = lastIndexOf(title, ".");
	if (dot < 0) return title;
	return substring(title, 0, dot);
}

// Returns the IDs of every open image except the active one, which stays active.
function getOtherImageIDs() {
	activeID = getImageID();
	ids = newArray(0);
	for (i = 1; i <= nImages; i++) {
		selectImage(i);
		if (getImageID() != activeID) ids = Array.concat(ids, getImageID());
	}
	selectImage(activeID);
	return ids;
}

// Closes every open image whose ID is not in keepIDs.
function closeAllExcept(keepIDs) {
	for (i = nImages; i >= 1; i--) {
		selectImage(i);
		id = getImageID();
		keep = false;
		for (k = 0; k < keepIDs.length; k++) if (keepIDs[k] == id) keep = true;
		if (!keep) close();
	}
}

// Splits the active image into single-channel windows "__ch1".."__chN" and returns N.
// A single-channel image is duplicated so the original is left untouched.
function splitChannels() {
	run("Select None");
	getDimensions(w, h, nCh, s, f);
	if (nCh == 1) {
		run("Duplicate...", "title=__ch1 duplicate");
		return 1;
	}
	title = getTitle();
	run("Split Channels");
	for (c = 1; c <= nCh; c++) {
		selectWindow("C" + c + "-" + title);
		rename("__ch" + c);
	}
	return nCh;
}

// Returns the window names "__ch1".."__chN".
function channelNames(n) {
	names = newArray(n);
	for (c = 1; c <= n; c++) names[c - 1] = "__ch" + c;
	return names;
}

// Merges the named windows (in order) into one composite image and makes it active.
function mergeChannels(names) {
	if (names.length == 1) {
		selectWindow(names[0]);
		return;
	}
	args = "";
	for (i = 0; i < names.length; i++) args = args + "c" + (i + 1) + "=[" + names[i] + "] ";
	run("Merge Channels...", args + "create");
}

// Returns true if channel c is in spec ("all" or a list such as "1,3").
function isChannelSelected(spec, c) {
	if (spec == "all") return true;
	parts = split(spec, ", ");
	for (i = 0; i < parts.length; i++) if (parseInt(parts[i]) == c) return true;
	return false;
}
