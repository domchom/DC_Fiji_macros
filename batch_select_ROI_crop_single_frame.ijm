// This script crops all open images to the user-selected ROI and saves them as TIFF files in a specified folder.

// Define the folder where cropped images will be saved
output_folder_path = "/Users/domchom/Documents/Bement_lab/Meeting:conferences/!Conferences/2023_ASCB/movies/";

while (nImages > 0) {
	// Get the name of the current image
    fileName = getTitle();
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_crop_one_frame.tif" ;
	
	// start the animation of the movie
	run("Animation Options...", "speed=50");
	doCommand("Start Animation [\\]");

	waitForUser("Select the ROI and frame for " + fileName);
	selectWindow(fileName);
	
	//crop the image to the ROI
	run("Duplicate...", " ");
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();

}