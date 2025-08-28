// Define LUTs for each channel
ch1_lut = "Red";
ch2_lut = "Cyan";
ch3_lut = "Green";
ch4_lut = "Magenta";

luts = newArray(ch1_lut, ch2_lut, ch3_lut, ch4_lut);

// Loop through all open images
while (nImages > 0) {

    getDimensions(width, height, channels, slices, frames);		
    // Save movie dimensions for later use
    fileName = getInfo("image.title"); 	
	imageName = getInfo("image.filename"); 
	selectWindow(fileName);
    Stack.setDisplayMode("composite");
	
	// Special case: if only one channel, force grayscale
    if (channels == 1) {
        Stack.setChannel(1);
        run("Grays");
        run("Enhance Contrast", "saturated=0.35");
        resetMinAndMax();

    } 
    else {
	    // Loop through all channels
	    for (c = 1; c <= channels; c++) {
	        Stack.setChannel(c);
	
			run(luts[c - 1]);
	        // Enhance contrast and reset intensity range
	        run("Enhance Contrast", "saturated=0.35");
	        resetMinAndMax();
	    }
    }    
    run("Save");
	close();
}