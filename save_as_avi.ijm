while (nImages > 0) {
	
	fileName = getInfo("image.filename") ; 
	//saves image name for future use
	path = getDirectory("image") ;
	//saves path that the image is saved to
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	//this and the above line get the file name without the extension
	newFileName = fileNameWithoutExtension + "_avi.avi" ;

	fullPath = path + "/" + newFileName;
	//creates a save path for the newly created file

	saveAs("Avi","/Users/chomchai/Documents/Bement_lab/Meetings/220510_prelim/Present/figures/binder/"+newFileName);	
	//save(fullPath) ;
	close();
					}