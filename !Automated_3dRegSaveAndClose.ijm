// !Automated_3dRegSaveAndClose.ijm
// Registers every open multi-channel time-lapse with PoorMan3DReg (translation).
// Channels are temporarily swapped into z so all channels are registered together
// on their max projection. Then LUTs are applied and the result is saved.
//
// Usage:  open the movies, edit the parameters below, run.
// Output: <name>_reg.tif
// Requires: PoorMan3DReg plugin.

// ===== PARAMETERS =====
output_folder_path = "/Volumes/DOM_SEVEN/2026AugBillData/080726_Pm-PLCPH-Ect2/"; // "" = ask
luts = newArray("Red", "Cyan", "Green", "Magenta");   // per channel; extra channels get Grays
// ======================

output_folder_path = prepareOutputFolder(output_folder_path);

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	baseName = getBaseName(getTitle());
	getDimensions(w, h, nCh, s, f);

	swap = "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]";
	run("Re-order Hyperstack ...", swap);
	run("PoorMan3DReg ", "transformation=Translation number=" + nCh + " projection=[Max Intensity]");
	run("Re-order Hyperstack ...", swap);

	if (nCh > 1) Stack.setDisplayMode("composite");
	for (c = 1; c <= nCh; c++) {
		Stack.setChannel(c);
		if (c <= luts.length) run(luts[c - 1]);
		else run("Grays");
		run("Enhance Contrast", "saturated=0.15");
	}

	saveAs("Tiff", output_folder_path + baseName + "_reg.tif");
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
