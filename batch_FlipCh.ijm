// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

ch_to_invert = 3;

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_Ch" + ch_to_invert + "flipped.tif" ;
	
	run("Split Channels");
	selectWindow("C" + ch_to_invert + "-" + imageName);
	run("Flip Horizontally", "stack");
	//run("Flip Vertically", "stack");
	
	if (channels == 2) {
	    run("Merge Channels...", "c1=C1-" + imageName + " c2=C2-" + imageName + " create");
		saveAs("Tiff", output_folder_path + newFileName);
		close();
	}
	
	if (channels == 3) {
	    run("Merge Channels...", "c1=C1-" + imageName + " c2=C2-" + imageName + " c3=C3-" + imageName + " create");
		saveAs("Tiff", output_folder_path + newFileName);
		close();
	    }
	if (channels == 4) {
    	run("Merge Channels...", "c1=C1-" + imageName + " c2=C2-" + imageName + " c3=C3-" + imageName + " c4=C4-" + imageName + " create");
		saveAs("Tiff", output_folder_path + newFileName);
		close();
    }
}