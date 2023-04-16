//this is accomp[lished by splitting the channels, and then deleting the second channel
//so this script only works for saving the first channel and not the sceond

// Define the folder where cropped images will be saved
output_folder_path = "/Volumes/DOM_LS/129DCE_230316_Rho-IT-waves-SFC/processed/t-series/raw_crop/";

while (nImages > 0) {

	// Get the name of the current image
    image_title = getTitle();
    
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	//this and the above line get the file name without the extension
	newFileName = image_title_without_extension + "_Ch1.tif" ;

	run("Split Channels");
	close();

	saveAs("Tiff", output_folder_path + newFileName);	
	close();
					}