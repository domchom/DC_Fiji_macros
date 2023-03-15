while (nImages > 0) {
	
	fileName = getInfo("image.filename") ; 
	//saves image name for future use
	path = getDirectory("image") ;
	//saves path that the image is saved to
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	//this and the above line get the file name without the extension
	newFileName = fileNameWithoutExtension + "_kymo.tif" ;

	fullPath = path + "/" + newFileName;
	//creates a save path for the newly created file

	saveAs("Tif","/Volumes/DOM_THREE/118DCE_230118_Ect2-Mgc-SFC/118processed/60x/reg-crop-better_ones_kymo/"+newFileName);	
	//save(fullPath) ;
	close();
					}