// !batch_ChangeFrameInterval.ijm
// Sets the frame interval (and optionally the pixel size) of every open image.
// NOTE: overwrites the original files in place.
//
// Usage:  open the images, edit the parameters below, run.

// ===== PARAMETERS =====
frame_interval = 3.83;        // seconds
pixel_size     = 0.2661449;   // in the image's units; 0 = leave unchanged
// ======================

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	Stack.setFrameInterval(frame_interval);
	if (pixel_size > 0) run("Properties...", "pixel_width=" + pixel_size + " pixel_height=" + pixel_size);
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
