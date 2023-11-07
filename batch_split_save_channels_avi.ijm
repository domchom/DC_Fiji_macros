//this is accomp[lished by splitting the channels, and then deleting the second channel
//so this script only works for saving the first channel and not the sceond

// Define the folder where cropped images will be saved
output_folder_path = "/Users/domchom/Documents/Bement_lab/Meeting:conferences/!Lab_Meetings/231009_tagged-Ect2_waves/SFC/raw/";

while (nImages > 0) {

	// Get the name of the current image
    image_title = getTitle();
    
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	//this and the above line get the file name without the extension
	newFileName0 = image_title_without_extension + ".avi" ;
	newFileName1 = image_title_without_extension + "_Ch1.avi" ;
	newFileName2 = image_title_without_extension + "_Ch2.avi" ;

	saveAs("Avi", output_folder_path + newFileName0);	
	
	run("Split Channels");
	run("Grays");
	run("Enhance Contrast", "saturated=0.35");
	saveAs("Avi", output_folder_path + newFileName2);	
	close();

	
	run("Grays");
	run("Enhance Contrast", "saturated=0.35");
	saveAs("Avi", output_folder_path + newFileName1);	
	close();
					}