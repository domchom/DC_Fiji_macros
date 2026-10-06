// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

ch_to_remove = 3;

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_Ch" + ch_to_remove + "removed.tif" ;
	
	run("Split Channels");
	selectWindow("C" + ch_to_remove + "-" + imageName);
	close();
	
	if (channels == 2) {
		saveAs("Tiff", output_folder_path + newFileName);
	}
	
	if (channels == 3) {
	    unused = newArray("","");
    	idx = 0;
    	for (c = 1; c <= channels; c++) {
	        if (c != ch_to_remove) {
	            unused[idx] = "C" + c + "-" + imageName;
	            idx++;
	        }
	    }
	    run("Merge Channels...", "c1=[" + unused[0] + "] c2=[" + unused[1] + "] create");
	    saveAs("Tiff", output_folder_path + newFileName);
	    close();
	    }
	if (channels == 4) {
    	// Collect all unused channels
    	unused = newArray("", "", "");
    	idx = 0;
    	for (c = 1; c <= channels; c++) {
	        if (c != ch_to_remove) {
	            unused[idx] = "C" + c + "-" + imageName;
	            idx++;
	        }
	    }
        run("Merge Channels...", 
        "c1=[" + unused[0] + "] " +
        "c2=[" + unused[1] + "] " +
        "c3=[" + unused[2] + "] create");

	    saveAs("Tiff", output_folder_path + newFileName);
	    close();
    }
}