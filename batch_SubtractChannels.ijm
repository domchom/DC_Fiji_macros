// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

//Note that the resulting image is saved to the final channel (so channel for a initally 4 channel image)
subtract_from_Ch = 2;
what_to_subtract = 1;

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames);		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	if (dotIndex == -1) {
	    fileNameWithoutExtension = imageName;
	} else {
	    fileNameWithoutExtension = substring(imageName, 0, dotIndex);
	}
	newFileName = fileNameWithoutExtension + "_subtractCh" + what_to_subtract + "fromCh" + subtract_from_Ch + ".tif" ;

	// Split the channels into separate images
	run("Split Channels");
	
	// Assume the channels are named "C1-", "C2-", etc.
	// Load Channel 1 and Channel 2
	minus_ch = "C" + what_to_subtract + "-" + imageName;
	start_ch = "C" + subtract_from_Ch + "-" + imageName;

	// Perform subtraction: Channel2 - Channel1
	imageCalculator("Subtract create stack", start_ch, minus_ch);
	
	// Rename the resulting image
	rename("subtraction_result");
	if (channels == 2) {
		saveAs("Tiff", output_folder_path + newFileName);
		close();
		close();
		close();
	}
	// Detect the unused channel (works for 3-channel images)
	if (channels == 3) {
	    unused = newArray("");
    	idx = 0;
    	for (c = 1; c <= channels; c++) {
	        if (c != subtract_from_Ch && c != what_to_subtract) {
	            unused[idx] = "C" + c + "-" + imageName;
	            idx++;
	        }
	    }
	    run("Merge Channels...", "c1=[" + unused[0] + "] c2=[subtraction_result] create");
	    saveAs("Tiff", output_folder_path + newFileName);
	    close();
	    close();
	    close();
	    }
	if (channels == 4) {
    	// Collect all unused channels
    	unused = newArray("", "");
    	idx = 0;
    	for (c = 1; c <= channels; c++) {
	        if (c != subtract_from_Ch && c != what_to_subtract) {
	            unused[idx] = "C" + c + "-" + imageName;
	            idx++;
	        }
	    }
        run("Merge Channels...", 
        "c1=[" + unused[0] + "] " +
        "c2=[" + unused[1] + "] " +
        "c3=[subtraction_result] create");

	    saveAs("Tiff", output_folder_path + newFileName);
	    close();
	    close();
	    close();
    }

}
