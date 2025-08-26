// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/!Embryos/256DCE_250109_emb_100ngGFP-rGBD_5uM-647-Dex_60x_SFC/!processed_images/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_subtract-c1-from-c2" + ".tif" ;
	
	// Fiji Macro: Subtract Channel 1 from Channel 2
	
	
	// Split the channels into separate images
	run("Split Channels");
	
	// Assume the channels are named "C1-", "C2-", etc.
	// Load Channel 1 and Channel 2
	selectWindow("C1-" + imageName);
	rename("Channel1");
	selectWindow("C2-" + imageName);
	rename("Channel2");
	
	// Perform subtraction: Channel2 - Channel1
	imageCalculator("Subtract create stack", "Channel2", "Channel1");
	
	// Rename the resulting image
	rename("Channel2_Subtracted_Channel1");
	
	// Close intermediate images if desired
	selectWindow("Channel1");
	close();
	selectWindow("Channel2");
	close();
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	
}
