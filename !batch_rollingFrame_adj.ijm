// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_SEVEN/389DCE_260813_mCh-Ect2_PIPs_SFC/!processed_images/test/";

// Configure rolling average
rolling_frames = 22;
scaling_factor = 0.85;

// Configure which channels to process
// Set to false to skip a channel
correctChannels = newArray(true, false, false, false); // C1, C2, C3, C4


while (nImages > 0) {

	getDimensions(width, height, channels, slices, frames);
	// gets and saves the movie dimensions for later use

	fileName = getInfo("image.title");
	// gets and saves the file name for later

	imageName = getInfo("image.filename");
	dotIndex = indexOf(imageName, ".");
	fileNameWithoutExtension = substring(imageName, 0, dotIndex);

	newFileName = fileNameWithoutExtension + "_rolling_corr" + ".tif";


	// =========================================================
	// SINGLE CHANNEL
	// =========================================================

	if (channels == 1) {

		// Rename original channel
		rename("C1");

		if (correctChannels[0]) {

			// Duplicate original movie
			run("Duplicate...", "title=dup duplicate channels=1-"+channels+" slices=1-"+slices+" frames=1-"+frames);
			
			rename("C1_original");

			// Create rolling average copy
			rrun("Duplicate...", "title=dup duplicate channels=1-"+channels+" slices=1-"+slices+" frames=1-"+frames);
			
			rename("C1_rolling");

			// Running ZProjector2
			run("Running ZProjector2", "project=" + rolling_frames + " projection=[Average Intensity]");

			// Multiply rolling average by 0.85
			run("Multiply...", "value=" + scaling_factor);

			rename("C1_background");

			// Subtract processed rolling average from original
			imageCalculator("Subtract create", "C1_original", "C1_background");

			rename("C1");

			// Close intermediate images
			selectWindow("C1_original");
			close();

			selectWindow("C1_background");
			close();
		}

		// Save processed movie
		selectWindow("C1");
		saveAs("Tiff", output_folder_path + newFileName);

		close();
	}


	// =========================================================
	// MULTI-CHANNEL
	// =========================================================

	else {

		run("Split Channels");

		// Loop through all channels
		for (c = 1; c <= channels; c++) {

			selectWindow("C" + c + "-" + fileName);

			// Rename channel
			rename("C" + c);

			if (correctChannels[c - 1]) {

				// ---------------------------------------------
				// Keep an untouched copy of the original
				// ---------------------------------------------

				run("Duplicate...", "title=C" + c + "_original");


				// ---------------------------------------------
				// Create rolling-average movie
				// ---------------------------------------------

				run("Duplicate...", "title=C" + c + "_rolling");

				// Running average over 12 frames
				run("Running ZProjector2", "rolling=" + rolling_frames);

				// Multiply rolling average by 0.85
				run("Multiply...", "value=" + scaling_factor);

				rename("C" + c + "_background");


				// ---------------------------------------------
				// Original - 0.85 * rolling average
				// ---------------------------------------------

				imageCalculator(
					"Subtract create",
					"C" + c + "_original",
					"C" + c + "_background"
				);

				rename("C" + c);


				// ---------------------------------------------
				// Close intermediate images
				// ---------------------------------------------

				selectWindow("C" + c + "_original");
				close();

				selectWindow("C" + c + "_background");
				close();
			}
		}


		// =====================================================
		// Merge channels dynamically
		// =====================================================

		if (channels == 2) {
			run("Merge Channels...", "c1=C1 c2=C2 create");
		}
		else if (channels == 3) {
			run("Merge Channels...", "c1=C1 c2=C2 c3=C3 create");
		}
		else if (channels == 4) {
			run("Merge Channels...", "c1=C1 c2=C2 c3=C3 c4=C4 create");
		}


		// Save merged processed movie
		saveAs("Tiff", output_folder_path + newFileName);


		// =====================================================
		// Close all windows
		// =====================================================

		for (c = 0; c < channels + 1; c++) {
			close();
		}
	}
}