// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/241202/!processed_images/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = "actual_MIP" + fileNameWithoutExtension + ".tif" ;
	
	run("Re-order Hyperstack ...", "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]");
	run("Z Project...", "projection=[Max Intensity] all");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
}
