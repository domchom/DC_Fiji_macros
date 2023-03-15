/*This script is used for creating a cropped region of all open images.
 * The user will open all the images they want to crop. 
 * The user will then be prompted to select the ROI for each image
*/
while (nImages > 0) {

	fileName = getInfo("image.filename") ; 
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	//this and the above line get the file name without the extension
	newFileName = fileNameWithoutExtension + "Crop.tif" ;

	doCommand("Start Animation [\\]");
	waitForUser("Select the ROI");
	selectWindow(fileName);
	run("Crop");
	saveAs("Tiff","/Volumes/DOM_LS/127DCE_230302_Ect2-GFP_dtom-rGBD_SFC_LS/SFC/processed/crop/"+newFileName);
	//change the above to save to a certain folder
	close();

}