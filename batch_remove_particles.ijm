output_folder_path = "/Users/domchom/Desktop/Isaac_data/003IHE_230414_FV_MgcdeltaGAP-waves/processed/raw_particles_removed/";

while (nImages > 0) {
	// Get the name of the current image
    fileName = getTitle();
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_particles-removed.tif" ;

	run("8-bit");
	setAutoThreshold("Default dark");
	//run("Threshold...");
	
	waitForUser("Set Threshold " + fileName);
		
	run("Analyze Particles...", "  show=Masks stack");
	
	selectWindow("Mask of " + fileName);
	run("Invert", "stack");

	imageCalculator("AND create stack",fileName,"Mask of " + fileName);
	selectWindow("Result of " + fileName);
	saveAs("Tiff", output_folder_path + newFileName);
	run("16-bit");
	
	close();
	close();
	close();
}
