// batch_TrimFrames.ijm
// Keeps only frames first_frame..last_frame (all channels and z) of every open movie.
//
// Usage:  open the movies, edit the parameters below, run.
// Output: <name>_frames<first>-<last>.tif

// ===== PARAMETERS =====
output_folder_path = "/Users/domchom/Documents/Bement_lab/Meeting:conferences/!Lab_Meetings/231120_tagged-Ect2_waves/"; // "" = ask
first_frame = 1;
last_frame  = 1;   // values past the end are clamped to the last frame
// ======================

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	baseName = getBaseName(getTitle());

	run("Select None");
	if (Stack.isHyperstack) {
		getDimensions(w, h, nCh, s, nFrames);
		last = minOf(last_frame, nFrames);
		run("Duplicate...", "title=__trim duplicate frames=" + first_frame + "-" + last);
	} else {
		last = minOf(last_frame, nSlices);
		run("Duplicate...", "title=__trim duplicate range=" + first_frame + "-" + last);
	}

	saveAs("Tiff", output_folder_path + baseName + "_frames" + first_frame + "-" + last + ".tif");
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
