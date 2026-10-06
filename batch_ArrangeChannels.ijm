// batch_ArrangeChannels.ijm
// Reorders, swaps or removes channels of every open image.
//   swap 1 and 2 (3-ch):  new_order = "213"
//   remove channel 3:     new_order = "12"
//   reverse (4-ch):       new_order = "4321"
//
// Usage:  open the images, edit the parameters below, run.
// Output: <name>_ch<new_order>.tif

// ===== PARAMETERS =====
output_folder_path = "/Volumes/DOM_SEVEN/!Ect2-FL-tagged-waves-vs-PIPs/!combined/ch1_PIPs_Ch2-Ect2/"; // "" = ask
new_order = "21";
// ======================

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	title = getTitle();
	baseName = getBaseName(title);

	getDimensions(w, h, nCh, s, f);
	if (!orderFits(new_order, nCh)) {
		print("Skipped (order " + new_order + " needs more than " + nCh + " channels): " + title);
		closeAllExcept(otherIDs);
		continue;
	}

	splitChannels();
	names = newArray(lengthOf(new_order));
	for (i = 0; i < lengthOf(new_order); i++) names[i] = "__ch" + substring(new_order, i, i + 1);
	mergeChannels(names);
	saveAs("Tiff", output_folder_path + baseName + "_ch" + new_order + ".tif");
	closeAllExcept(otherIDs);
}

// Returns true if every digit in order is a valid channel number (1..nCh).
function orderFits(order, nCh) {
	for (i = 0; i < lengthOf(order); i++) {
		c = parseInt(substring(order, i, i + 1));
		if (isNaN(c) || c < 1 || c > nCh) return false;
	}
	if (nCh < 2) return false;
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
