// batch_ChangeImageType.ijm
// Converts every open image to the given bit depth (all channels).
// NOTE: overwrites the original files in place.
//
// Usage:  open the images, edit the parameters below, run.

// ===== PARAMETERS =====
image_type = "16-bit";   // "8-bit", "16-bit" or "32-bit"
// ======================

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	run(image_type);
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
