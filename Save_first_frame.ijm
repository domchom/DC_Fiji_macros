while (nImages > 0) {

	//this is accomp[lished by splitting the channels, and then deleting the second channel
	//so this script only works for saving the first channel and not the sceond
	fileName = getInfo("image.filename") ; 
	//saves image name for future use
	path = getDirectory("image") ;
	//saves path that the image is saved to
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	//this and the above line get the file name without the extension
	newFileName = fileNameWithoutExtension + "_first_frame.tif" ;

	fullPath = path + "/" + newFileName;
	//creates a save path for the newly created file

	run("Duplicate...", "duplicate range=15");


	saveAs("Tiff","/Users/domchom/Desktop/Cell_profile/WavesIdentification/"+newFileName);	
	close();
					}