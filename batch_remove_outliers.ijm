output_folder_path = "/Volumes/DOM_FIVE/159DCE/processed/raw_crop_edited/";

while (nImages > 0) {
	
	// Get the name of the current image
    fileName = getTitle();
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_removed_outliers.tif" ;

	run("Remove Outliers...", "radius=2 threshold=200 which=Bright stack");
	saveAs("Tiff", output_folder_path + newFileName);
	close();

}