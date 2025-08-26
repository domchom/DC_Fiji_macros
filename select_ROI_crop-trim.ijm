// This script crops all open images to the user-selected ROI and saves them as TIFF files in a specified folder.

// Define the folder where cropped images will be saved
output_folder_path = "/Users/domchom/Desktop/";

i = 1;

while (nImages > 0) {
	// Get the name of the current image
    fileName = getTitle();
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	getDimensions(width, height, channels, slices, frames);
	
	// start the animation of the movie
	//run("Animation Options...", "speed=30");
	//doCommand("Start Animation [\\]");

	waitForUser("Select the ROI to crop and beginning frame to trim");
	total_frames = nSlices / channels;
	currentFrame = getSliceNumber();
	first_frame = currentFrame / channels;
	last_frame = currentFrame + 199;
	
	selectWindow(fileName);
	
	//crop the image to the ROI
	run("Duplicate...", " duplicate range=" + first_frame + "-" + last_frame);
	
	// Ensure the number of frames is even
	num_frames = nSlices / channels;
    if (num_frames % 2 != 0) {
    	new_last_frame = num_frames - 1;
    	new_ori_last_frame = last_frame - 1;
        run("Duplicate...", " duplicate range=" + 1 + "-" + new_last_frame);
        newFileName = fileNameWithoutExtension + "_ROI-" + i + "_frames" + first_frame + "-" + new_ori_last_frame + ".tif" ;
        saveAs("Tiff", output_folder_path + newFileName);
		close();
		close();
    } else {
    	newFileName = fileNameWithoutExtension + "_ROI-" + i + "_frames" + first_frame + "-" + last_frame + ".tif" ;
    	saveAs("Tiff", output_folder_path + newFileName);
		close();
	}
	i += 1;

}