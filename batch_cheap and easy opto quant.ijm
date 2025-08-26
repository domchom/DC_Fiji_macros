//This macro uses the image properties to calculate the wave speed, so ensure that the
//units are correct, and that the frame itnerval and the pixel size is correct.

//To use, open each movie that you want to measure, and then run the script. It will ask you
//create lines and add them to the ROI manager. You can add as many as you wish. It wlll then
//calculate the wave speed for each line, and then calculate the average wave speed.

roiManager("reset");

// Wait for the user to draw a line
waitForUser("select ROI for opto activation...");

roiManager("Add");

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
		
	run("Clear Results");
	
	run("Split Channels");
	
	IJ.log("Processing " + fileNameWithoutExtension);
	roiManager("select", 0);
	setSlice(6);
	run("Measure");
	// Get the mean value from the results table
	ch2_mean = getResult("Mean", nResults - 1);
	
	run("Clear Results");
	
	roiManager("select", 0);
	setSlice(5);
	run("Measure");
	// Get the new mean value and add to list
	ch2_meanAtFrame5 = getResult("Mean", nResults - 1);
	
	close();
	
	roiManager("select", 0);
	setSlice(6);
	run("Measure");
	ch1_mean = getResult("Mean", nResults - 1);
	
	roiManager("select", 0);
	setSlice(5);
	run("Measure");
	ch1_meanAtFrame5 = getResult("Mean", nResults - 1);
	
	run("Clear Results");
	
	ch1_activation_ratio = ch1_mean / ch1_meanAtFrame5;
	ch2_activation_ratio = ch2_mean / ch2_meanAtFrame5;
	
	// Add a new row and display the ratios in the Results table
    rowIndex = nResults;  // Get the current number of results (rows) in the table
    setResult("FileName", rowIndex, fileNameWithoutExtension);
    setResult("ch1_post:pre_ratio", rowIndex, ch1_activation_ratio);
    setResult("ch2_post:pre_ratio", rowIndex, ch2_activation_ratio);
    updateResults();
	
	// Display the ratio
	IJ.log("ch2 post:pre ratio: " + ch2_activation_ratio);
	IJ.log("ch1 post:pre ratio: " + ch1_activation_ratio);
	
	close();
}
