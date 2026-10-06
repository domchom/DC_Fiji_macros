//This macro uses the image properties to calculate the wave speed, so ensure that the
//units are correct, and that the frame itnerval and the pixel size is correct.

//To use, open each movie that you want to measure, and then run the script. It will ask you
//create lines and add them to the ROI manager. You can add as many as you wish. It wlll then
//calculate the wave speed for each line, and then calculate the average wave speed.

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	
	fileName = getInfo("image.filename") ; 
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	//this and the above line get the file name without the extension
	//newFileName = fileNameWithoutExtension + "_KymScaleY4.tif" ;
	
	IJ.log("Processing " + fileNameWithoutExtension);
	
	roiManager("reset");

	// Wait for the user to draw a line
	waitForUser("Add lines to ROI Manager...");
	
	num_ROIs = roiManager("size");
	
	total_slope = 0;
	
	for (i=0; i < num_ROIs; i++) {
		RoiManager.select(i)
		getLine(x1, y1, x2, y2, lineWidth);
		getPixelSize(unit, pixelWidth, pixelHeight);
		frame_interval = Stack.getFrameInterval();
		
		x1 = x1 * pixelWidth;
		x2 = x2 * pixelWidth;
		y1 = y1 * frame_interval;
		y2 = y2 * frame_interval;
		
		// Measure the length of the line
		slope =  (x2 - x1) / (y2 - y1);
		slope = abs(slope);
		
		total_slope += slope;
		idx = i + 1;
				
		// Display the slope
		IJ.log("line " + idx + ": " + slope + "um/s");
	}
    
    average_slope = total_slope / num_ROIs;
    IJ.log("average slope: " + average_slope + "um/s");
    	
    close();
}
