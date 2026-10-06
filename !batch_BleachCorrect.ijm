// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_SIX/!dom_analysis/raw_bleachCorr/";
correction_type = "Exponential Fit"
//correction_type = "Histogram Matching"
//Histogram matching takes much longer

// Configure which channels to correct (set to false to skip)
correctChannels = newArray(true, true, false, false); // C1, C2, C3, C4

// Returns true if the active image's mean intensity decays over time.
// Mirrors the check the Bleach Correction plugin does for Exponential Fit
// (y = a*exp(-bx) + c must have b > 0), so we can skip instead of erroring.
function isDecaying() {
	n = nSlices;
	if (n < 3) return false;
	x = newArray(n);
	y = newArray(n);
	for (i = 1; i <= n; i++) {
		setSlice(i);
		getStatistics(area, mean);
		x[i - 1] = i - 1;
		y[i - 1] = mean;
	}
	setSlice(1);
	Fit.doFit("Exponential with offset", x, y);
	decayRate = Fit.p(1);
	if (decayRate <= 0) return false;
	if (y[n - 1] >= y[0]) return false;
	return true;
}

// Returns true if id is in the array ids
function contains(ids, id) {
	for (i = 0; i < ids.length; i++) {
		if (ids[i] == id) return true;
	}
	return false;
}

while (nImages > 0) {
	currentID = getImageID();
	// Remember the other images still queued so we only close what this file created
	otherIDs = newArray(0);
	for (i = 1; i <= nImages; i++) {
		selectImage(i);
		if (getImageID() != currentID) otherIDs = Array.concat(otherIDs, getImageID());
	}
	selectImage(currentID);

	getDimensions(width, height, channels, slices, frames);
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title");
	//gets and saves the file name for later

	imageName = getInfo("image.filename") ;
	dotIndex = indexOf(imageName, ".");
	fileNameWithoutExtension = substring(imageName, 0, dotIndex);
	newFileName = fileNameWithoutExtension + "_bleach_corr" + ".tif" ;

	// Special case: if only one channel, force grayscale
    if (channels == 1) {
        if (isDecaying()) {
        	run("Bleach Correction", "correction=[Exponential Fit]");
        } else {
        	print("Skipped (no decay): " + fileName);
        }
        saveAs("Tiff", output_folder_path + newFileName);
    }
    else {
    	run("Split Channels");
	    // Loop through all channels
	    for (c = 1; c <= channels; c++) {
	        selectWindow("C" + c + "-" + fileName);
	        if (correctChannels[c - 1]) {
	        	if (correction_type != "Exponential Fit" || isDecaying()) {
	        		run("Bleach Correction", "correction=[" + correction_type + "]");
	        	} else {
	        		print("Skipped C" + c + " (no decay): " + fileName);
	        	}
	        }
			rename("C" + c);
	    }
	    // Merge channels dynamically
	    if (channels == 2) {
	    	run("Merge Channels...", "c1=C1 c2=C2 create");
	    }
	    else if (channels == 3) {
	    	run("Merge Channels...", "c1=C1 c2=C2 c3=C3 create");
	    }
	    else if (channels == 4) {
	    	run("Merge Channels...", "c1=C1 c2=C2 c3=C3 c4=C4 create");
	    }
	    saveAs("Tiff", output_folder_path + newFileName);
    }

    // Close every window this file produced (originals, corrected copies, fit plots)
    for (i = nImages; i >= 1; i--) {
    	selectImage(i);
    	if (!contains(otherIDs, getImageID())) close();
    }
}
