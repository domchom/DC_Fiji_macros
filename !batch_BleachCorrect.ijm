// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_bleach_corr" + ".tif" ;
	
	// Special case: if only one channel, force grayscale
    if (channels == 1) {
        run("Bleach Correction", "correction=[Exponential Fit]");
        saveAs("Tiff", output_folder_path + newFileName);
        close();
        close();
        close();

    } 
    else {
    	run("Split Channels");
	    // Loop through all channels
	    for (c = 1; c <= channels; c++) {
	        selectWindow("C" + c + "-" + fileName);
	        if (c = 2) {
	        	run("Bleach Correction", "correction=[Exponential Fit]");
	        }
			run("Bleach Correction", "correction=[Exponential Fit]");
			// Above 4 lines of code can be used or altered to skip bleach correction on any of the channels
			// This might be needed if one channel does not have anything to correct
			rename("C" + c);
	    }
	    if (channels == 2) {
	    	run("Merge Channels...", "c1=C1 c2=C2 create");
	    	saveAs("Tiff", output_folder_path + newFileName);
	    	close();
        	close();
        	close();
        	close();
        	close();
	    }
	    if (channels == 3) {
	    	run("Merge Channels...", "c1=C1 c2=C2 c3=C3 create");
	    	saveAs("Tiff", output_folder_path + newFileName);
	    	close();
        	close();
        	close();
        	close();
        	close();
        	close();
        	close();
	    }
	    if (channels == 4) {
	    	run("Merge Channels...", "c1=C1 c2=C2 c3=C3 c4=C4 create");
	    	saveAs("Tiff", output_folder_path + newFileName);
	    	close();
        	close();
        	close();
        	close();
        	close();
        	close();
        	close();
        	close();
        	close();
	    }
    }    
}