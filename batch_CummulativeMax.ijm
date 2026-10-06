// Creates cumulative max-projection Z stacks from all open images
// Each slice = max projection of that slice and every slice below it

// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_SEVEN/402DCE_260922_C1-488phal_C2-568-pMyo_FV/!processed_images/CummulativeMaxProject/";

setBatchMode(true);

while (nImages > 0) {
	originalID = getImageID();
	getDimensions(width, height, channels, slices, frames);
	
	title = getTitle();
	dotIndex = lastIndexOf(title, ".");
	if (dotIndex < 0) dotIndex = lengthOf(title);
	fileNameWithoutExtension = substring(title, 0, dotIndex);
	newFileName = fileNameWithoutExtension + "_cumMax.tif";

	mergeString = "";
	counter = 1;
	while (counter <= channels) {
		selectImage(originalID);
		if (channels > 1) Stack.setChannel(counter);
		run("Duplicate...", "title=cum" + counter + " duplicate channels=" + counter);
		
		n = nSlices;
		for (i = 2; i <= n; i++) {
			selectWindow("cum" + counter);
			setSlice(i - 1);
			run("Duplicate...", "title=prev");
			selectWindow("cum" + counter);
			setSlice(i);
			imageCalculator("Max", "cum" + counter, "prev");
			close("prev");
		}
		
		mergeString = mergeString + " c" + counter + "=cum" + counter;
		counter += 1;
	}

	if (channels > 1) {
		run("Merge Channels...", mergeString + " create");
	} else {
		selectWindow("cum1");
	}

	Stack.setSlice(1);
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	selectImage(originalID);
	close();
}

setBatchMode(false);