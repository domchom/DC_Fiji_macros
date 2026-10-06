// batch_SelectCropSingleframe.ijm
// Interactive single-frame crop: plays each open movie, waits for you to pick a
// frame and draw a selection, then saves that frame (all channels and z) cropped.
//
// Usage:  open the movies, edit the parameters below, run. Stop on the frame you
//         want, draw a selection, click OK. With no selection the full frame is saved.
// Output: <name>_crop_one_frame.tif

// ===== PARAMETERS =====
output_folder_path = "/Users/domchom/Documents/Bement_lab/Meeting:conferences/!Conferences/2023_ASCB/movies/Ect2 PH mutatnts/"; // "" = ask
preview_speed = 50;   // playback fps while choosing
// ======================

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	inputID = getImageID();
	title = getTitle();
	baseName = getBaseName(title);

	run("Animation Options...", "speed=" + preview_speed);
	doCommand("Start Animation [\\]");
	waitForUser("Pick the frame and select the ROI for " + title);
	selectImage(inputID);

	if (Stack.isHyperstack) {
		Stack.getPosition(ch, sl, fr);
		run("Duplicate...", "title=__frame duplicate frames=" + fr);
	} else {
		run("Duplicate...", "title=__frame");
	}
	saveAs("Tiff", output_folder_path + baseName + "_crop_one_frame.tif");
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
