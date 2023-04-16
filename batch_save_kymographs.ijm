// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/macro_testing/noise/";

while (nImages > 0) {
	// Get the name of the current image
    image_title = getTitle();
    
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	newFileName = image_title_without_extension + "_kymo.tif" ;

	saveAs("Tif", output_folder_path + newFileName);	
	close();
					}