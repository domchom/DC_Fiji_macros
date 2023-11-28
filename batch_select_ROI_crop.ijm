// This script crops all open images to the user-selected ROI and saves them as TIFF files in a specified folder.

// Define the folder where cropped images will be saved
output_folder_path = "/Volumes/T7/!Rho-IT_200v1000ng-Ect2_waves/180DCE_200v1000_Rho-IT_waves_LS-only/processed/raw_3dReg_diff/kymo/crop/";

while (nImages > 0) {
	// Get the name of the current image
    fileName = getTitle();
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_crop.tif" ;
	
	// start the animation of the movie
	run("Animation Options...", "speed=50");
	doCommand("Start Animation [\\]");

	waitForUser("Select the ROI for to crop");
	selectWindow(fileName);
	
	//crop the image to the ROI
	run("Crop");
	saveAs("Tiff", output_folder_path + newFileName);
	close();

}