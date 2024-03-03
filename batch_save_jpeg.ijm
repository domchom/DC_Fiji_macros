// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Documents/Bement_lab/Papers/Rho-IT_waves_paper/data/sup_data/";

while (nImages > 0) {
	
	// Get the name of the current image
    image_title = getTitle();
    
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	// Define new filename
	newFileName = image_title_without_extension + ".jpg" ;

	saveAs("JPEG",output_folder_path + newFileName);	
	close();
					}