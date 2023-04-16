// Define the folder where cropped images will be saved
output_folder_path = "/Users/domchom/Desktop/macro_testing/noise/";

beginning_frame = "15";
end_frame = "1000"; // set the end frame to a large number initially

for (i = 0; nImages > 0; i++) {
		
	// Get the name of the current image
    image_title = getTitle();
    
    selectWindow(image_title);
 
    // Remove the file extension from the image title
	dot_index = indexOf(image_title, ".");  
	image_title_without_extension = substring(image_title, 0, dot_index); 
	
	//this and the above line get the file name without the extension
	newFileName = image_title_without_extension + "_frames" + beginning_frame + "-" + end_frame + ".tif" ;
		
	run("Duplicate...", "duplicate frames=" + beginning_frame + "-" + end_frame);
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
	
					}