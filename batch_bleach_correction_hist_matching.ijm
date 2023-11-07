// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/173DCE/SFC/processed/raw/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_bleach_corr" + ".tif" ;
	setOption("ScaleConversions", true);
	run("8-bit");
	run("Bleach Correction", "correction=[Histogram Matching]");

	
	saveAs("Tiff", output_folder_path + newFileName);

	close(); // comment out if doing one channel
	close(); // comment out if doing one channel
	// close(); // comment out if doing one channel

}
	