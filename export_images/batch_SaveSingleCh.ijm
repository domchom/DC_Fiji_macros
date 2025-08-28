// Define the folder where cropped images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

channel_to_save = 1;

while (nImages > 0) {

	// Get the name of the current image
    image_title = getTitle();
    getDimensions(width, height, channels, slices, frames);		

    // Remove the file extension from the image title
    dot_index = lastIndexOf(image_title, ".");  
    if (dot_index == -1) dot_index = lengthOf(image_title); // handle case w/ no extension
    image_title_without_extension = substring(image_title, 0, dot_index); 
    
    // Split into channels
    run("Split Channels");

    // Loop through however many channels were split
    for (i = 1; i <= channels; i++) {
    	if (i == channel_to_save) {
    		selectWindow("C" + i + "-" + image_title);
        	run("Grays");
        	run("Enhance Contrast", "saturated=0.35");
        	saveAs("Tiff", output_folder_path + image_title_without_extension + "_Ch" + i + ".tif");
    	}
        
        close();
    }
}