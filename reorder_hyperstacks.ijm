while (nImages > 0) {
	
	fileName = getInfo("image.filename") ; 
	//saves image name for future use
	path = getDirectory("image") ;
	//saves path that the image is saved to
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	//this and the above line get the file name without the extension

	fullPath = path + "/" + fileName;
	//creates a save path for the newly created file
	
	run("Re-order Hyperstack ...", "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]");
	saveAs("Tiff","/Users/domchom/Desktop/stacks/flipped_again/"+fileName);	
	//save(fullPath) ;
	close();
					}

