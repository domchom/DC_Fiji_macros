// Define frame interval
frame_int = "3.83";

// Loop through all open images
while (nImages > 0) {

    getDimensions(width, height, channels, slices, frames);		
    // Save movie dimensions for later use
    fileName = getInfo("image.title"); 	
	imageName = getInfo("image.filename"); 
	selectWindow(fileName);
	
	run("Properties...", "channels=" + channels + " slices=" + slices + " frames=" + frames + " pixel_width=0.2661449 pixel_height=0.2661449 voxel_depth=1.0000000 frame=" + frame_int);   
    run("Save");
	close();
}