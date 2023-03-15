
while (nImages > 0) {
	
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	path = getInfo("image.directory");  // use the source directory...
	//path = "/Users/bementmbp/Desktop" // ...or paste a custom save path

	imageName = getInfo("image.filename") ; 
	//saves image name for future use
	dotIndex = indexOf(imageName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	//this and the above line get the file name without the extension
	newFileName = fileNameWithoutExtension + "_trim" + ".tif" ;
	
	run("Duplicate...", "duplicate frames=10-" + frames);
	saveAs("Tiff","/Volumes/DOM_LS/125DCE_230224_Rho-IT-waves_SFC/processed/waves_only/trimmed/"+newFileName);
	close();
	close();
	
					}