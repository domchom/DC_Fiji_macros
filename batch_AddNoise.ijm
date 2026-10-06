// This script takes a group of images that are already opened in Fiji
// and then adds noise based on the "Add Specified Noise..." command
// it then saves it to a specified path

//To use this code, open all images that you want to process and define the output path and noise level below

// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/macro_testing/noise/";

// Define the noise level
noise_level = 1000; // Change this value to adjust the noise level

while (nImages > 0) {
	// Get the name of the current image
    image_title = getTitle();
    
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	// Define the new file name with the noise level
	new_file_name = image_title_without_extension + "_noise" + noise_level + ".tif" ;
	
	// Add noise to the image
	run("Add Specified Noise...", "stack standard=" + noise_level);
	
	// Save the image to the specified folder
	save_path = output_folder_path + new_file_name;
	saveAs("Tiff", save_path);
	
	// Close the current image to move on to the next one
	close();
}
