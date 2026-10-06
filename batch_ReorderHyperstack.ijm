// batch_ReorderHyperstack.ijm
// Swaps two hyperstack dimensions of every open image (e.g. to fix files where z
// and t were mixed up), optionally followed by a max projection over z.
//
// Usage:  open the images, edit the parameters below, run.
// Output: <name>_reordered.tif   or   <name>_MIP.tif when max_project = true

// ===== PARAMETERS =====
output_folder_path = "/Users/domchom/Desktop/241202/!processed_images/"; // "" = ask
swap        = "z-t";   // "z-t", "c-z" or "c-t"
max_project = false;   // max-project over z (all frames) after swapping
// ======================

if      (swap == "z-t") order = "channels=[Channels (c)] slices=[Frames (t)] frames=[Slices (z)]";
else if (swap == "c-z") order = "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]";
else if (swap == "c-t") order = "channels=[Frames (t)] slices=[Slices (z)] frames=[Channels (c)]";
else exit("Unknown swap: " + swap);

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	baseName = getBaseName(getTitle());

	run("Re-order Hyperstack ...", order);
	suffix = "_reordered";
	if (max_project) {
		run("Z Project...", "projection=[Max Intensity] all");
		suffix = "_MIP";
	}

	saveAs("Tiff", output_folder_path + baseName + suffix + ".tif");
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
