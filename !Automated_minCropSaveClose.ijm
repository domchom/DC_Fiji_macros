// Define the folder where cropped images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

while (nImages > 0) {

	getDimensions(width, height, channels, slices, frames) ;		
	fileName = getInfo("image.filename") ; 
	dotIndex = indexOf(fileName, ".");  
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_crop.tif" ;
	
	run("Z Project...", "projection=[Min Intensity]");
	selectWindow("MIN_" + fileName);
	
	if (channels > 1) {
		run("Z Project...", "projection=[Max Intensity]");	
		selectWindow("MAX_MIN_" + fileName);			

    } 
	
	setThreshold(1, 65535);
	run("Convert to Mask");
	run("Analyze Particles...", "add");
	selectWindow(fileName);
	roiManager("Select", 0);
	run("Crop");
	run("Select None");
	saveAs("Tiff",output_folder_path+newFileName);
	close();
	
	selectWindow("MIN_" + fileName);
	close();
	
	if (channels > 1) {
		selectWindow("MAX_MIN_" + fileName); 	
		close();

    } 
	
	roiManager("Delete");
	
					}