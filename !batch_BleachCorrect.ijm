// !batch_BleachCorrect.ijm
// Bleach-corrects the selected channels of every open image.
// With Exponential Fit, channels whose mean intensity does not decay are skipped
// (the plugin would otherwise error).
//
// Usage:  open the images, edit the parameters below, run.
// Output: <name>_bleach_corr.tif
// Requires: Bleach Correction plugin (CorrectBleach).

// ===== PARAMETERS =====
output_folder_path  = "/Volumes/DOM_SIX/!dom_analysis/raw_bleachCorr/"; // "" = ask
channels_to_process = "1,2";   // "all" or a list, e.g. "1,3"
correction_type     = "Exponential Fit";   // or "Histogram Matching" (much slower)
// ======================

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	title = getTitle();
	baseName = getBaseName(title);

	nCh = splitChannels();
	names = channelNames(nCh);
	for (c = 1; c <= nCh; c++) {
		if (!isChannelSelected(channels_to_process, c)) continue;
		selectWindow("__ch" + c);
		if (correction_type == "Exponential Fit" && !isDecaying()) {
			print("Skipped C" + c + " (no decay): " + title);
			continue;
		}
		run("Bleach Correction", "correction=[" + correction_type + "]");
		rename("__corr" + c);
		names[c - 1] = "__corr" + c;
	}
	mergeChannels(names);

	saveAs("Tiff", output_folder_path + baseName + "_bleach_corr.tif");
	closeAllExcept(otherIDs);   // also closes the fit plots
}

// Returns true if the active stack's mean intensity decays over time.
// Mirrors the plugin's Exponential Fit check (y = a*exp(-bx) + c needs b > 0).
function isDecaying() {
	n = nSlices;
	if (n < 3) return false;
	x = newArray(n);
	y = newArray(n);
	for (i = 1; i <= n; i++) {
		setSlice(i);
		getStatistics(area, mean);
		x[i - 1] = i - 1;
		y[i - 1] = mean;
	}
	setSlice(1);
	Fit.doFit("Exponential with offset", x, y);
	if (Fit.p(1) <= 0) return false;
	if (y[n - 1] >= y[0]) return false;
	return true;
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
