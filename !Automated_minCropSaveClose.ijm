// !Automated_minCropSaveClose.ijm
// Crops every open (registered) movie to the area that has signal in every frame,
// i.e. trims the zero-filled borders left by registration.
// Uses the bounding box of non-zero pixels in the min projection of channel 1.
//
// Usage:  open the movies, edit the parameters below, run.
// Output: <name>_crop.tif

// ===== PARAMETERS =====
output_folder_path = "/Volumes/DOM_SEVEN/384DCE_260731_PI-kinase-test_SFC/!processed_images/raw_reg_min/"; // "" = ask
// ======================

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	inputID = getImageID();
	baseName = getBaseName(getTitle());

	run("Select None");
	run("Duplicate...", "title=__c1 duplicate channels=1");
	run("Z Project...", "projection=[Min Intensity]");
	if (bitDepth() == 32) setThreshold(1e-9, 1e30);
	else setThreshold(1, pow(2, bitDepth()) - 1);
	run("Create Selection");
	getSelectionBounds(x, y, w, h);

	selectImage(inputID);
	makeRectangle(x, y, w, h);
	run("Crop");
	run("Select None");

	saveAs("Tiff", output_folder_path + baseName + "_crop.tif");
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
