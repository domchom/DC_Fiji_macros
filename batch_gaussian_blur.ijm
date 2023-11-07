// This will add a gaussian blur to all the open movies in Fiji

// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_FIVE/167=DELETE/processed/";

// Define the sigma level
sigma = 2.0; // Change this value to adjust the sigma level

while (nImages > 0) {

	// Get the name of the current image
    image_title = getTitle();
    
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	// Define the new file name with the noise level
	newFileName = image_title_without_extension + "_gaus-blur-" + sigma + ".tif" ;
	
	run("Gaussian Blur...", "sigma=" + sigma + " stack");
	saveAs("Tiff", output_folder_path + newFileName);
	close();
}


