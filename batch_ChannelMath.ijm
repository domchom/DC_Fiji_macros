// batch_ChannelMath.ijm
// Computes  channel_a <operation> channel_b  for every open image.
// The result is added as the last channel. Channels a and b are dropped
// unless keep_inputs = true.
// Divide is done in 32-bit (other channels are converted to match).
// Subtract keeps the original bit depth (negative values clip to 0).
//
// Usage:  open the images, edit the parameters below, run.
// Output: <name>_<a><op><b>.tif   e.g. _C1-C2.tif, _C1divC2.tif

// ===== PARAMETERS =====
output_folder_path = "/Volumes/DOM_SEVEN/376DCE_260707_embryo_controlvWTvWA_SFC/!processed_images/raw_c1-c2/"; // "" = ask
operation   = "Subtract";   // "Subtract" or "Divide"
channel_a   = 1;
channel_b   = 2;
keep_inputs = false;
// ======================

output_folder_path = prepareOutputFolder(output_folder_path);
if (operation == "Divide") { calcOp = "Divide create 32-bit stack"; tag = "div"; }
else                       { calcOp = "Subtract create stack";       tag = "-";   }

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	title = getTitle();
	baseName = getBaseName(title);

	getDimensions(w, h, nCh, s, f);
	if (channel_a > nCh || channel_b > nCh) {
		print("Skipped (only " + nCh + " channels): " + title);
		closeAllExcept(otherIDs);
		continue;
	}

	splitChannels();
	imageCalculator(calcOp, "__ch" + channel_a, "__ch" + channel_b);
	rename("__result");

	names = newArray(0);
	for (c = 1; c <= nCh; c++) {
		if (!keep_inputs && (c == channel_a || c == channel_b)) continue;
		if (operation == "Divide") {
			selectWindow("__ch" + c);
			run("32-bit");   // Merge Channels needs matching bit depths
		}
		names = Array.concat(names, "__ch" + c);
	}
	names = Array.concat(names, "__result");
	mergeChannels(names);

	saveAs("Tiff", output_folder_path + baseName + "_C" + channel_a + tag + "C" + channel_b + ".tif");
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
