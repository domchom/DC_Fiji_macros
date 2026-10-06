// !batch_ChangeLUTs.ijm
// Applies per-channel LUTs and resets display ranges for every open image.
// Single-channel images are set to Grays.
// NOTE: overwrites the original files in place.
//
// Usage:  open the images, edit the parameters below, run.

// ===== PARAMETERS =====
luts = newArray("Red", "Cyan", "Green", "Magenta");   // per channel; extra channels get Grays
// ======================

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	getDimensions(w, h, nCh, s, f);

	if (nCh == 1) {
		run("Grays");
		resetMinAndMax();
	} else {
		Stack.setDisplayMode("composite");
		for (c = 1; c <= nCh; c++) {
			Stack.setChannel(c);
			if (c <= luts.length) run(luts[c - 1]);
			else run("Grays");
			resetMinAndMax();
		}
	}

	run("Save");
	closeAllExcept(otherIDs);
}


// ===== HELPERS =====

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
