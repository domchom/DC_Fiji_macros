while (nImages > 0) {

	//this script only works for two channel movies
	//this script is used for converting two/three channel movies into one channel movies
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
	newFileName = fileNameWithoutExtension + "_C1only.tif" ;

	fullPath = path + "/" + newFileName;
	//creates a save path for the newly created file

	run("Split Channels");
	close();

	saveAs("Tiff","/Users/chomchai/Desktop/test_image_process_datasets/"+newFileName);	
	//save(fullPath) ;
	close();
					}