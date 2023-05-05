// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_FIVE/136DCE_230419_IT-Rho-waves-side-SFC/processed/c1_c2/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_c1_c2.tif" ;
	
	run("Split Channels");
	close();
	
	run("Merge Channels...", "c1=C1-" + fileName + " c2=C2-" + fileName + " create");
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	
}