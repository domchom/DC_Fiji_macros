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
	newFileName = fileNameWithoutExtension + "_div-by-sum" + ".tif" ;
	
	// Special case: if only one channel, force grayscale
    if (channels == 1) {
        run("Z Project...", "projection=[Sum Slices]");
		imageCalculator("Divide create 32-bit stack", "C1","SUM_C1");
		rename("result");
		run("16-bit");
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
	        rename("C" + c);
	        run("Z Project...", "projection=[Sum Slices]");
	        rename("SUM_C" + c);
			imageCalculator("Divide create 32-bit stack", "C" + c,"SUM_C" + c);
			rename("C" + c + "_result");
		}
	    if (channels == 2) {
	    	run("Merge Channels...", "c1=C1_result c2=C2_result create");
	    	saveAs("Tiff", output_folder_path + newFileName);
	    	close();
        	close();
        	close();
        	close();
        	close();
	    }
	    if (channels == 3) {
	    	run("Merge Channels...", "c1=C1_result c2=C2_result c3=C3_result create");
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
	    	run("Merge Channels...", "c1=C1_result c2=C2_result c3=C3_result c4=C4_result create");
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