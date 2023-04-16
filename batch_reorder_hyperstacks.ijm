// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/macro_testing/noise/";

while (nImages > 0) {
	// Get the name of the current image
    image_title = getTitle();
    
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	// Define the new file name
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 

	fullPath = path + "/" + fileName;
	//creates a save path for the newly created file
	
	run("Re-order Hyperstack ...", "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]");
	saveAs("Tiff",output_folder_path + fileName);	
	close();
					}

