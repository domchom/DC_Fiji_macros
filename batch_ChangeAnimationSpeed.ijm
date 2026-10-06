// batch_ChangeAnimationSpeed.ijm
// Sets the animation speed (playback fps) of every open movie.
// NOTE: overwrites the original files in place.
//
// Usage:  open the movies, edit the parameters below, run.

// ===== PARAMETERS =====
animation_speed = 30;   // frames per second
// ======================

while (nImages > 0) {
	otherIDs = getOtherImageIDs();
	run("Animation Options...", "speed=" + animation_speed);
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
