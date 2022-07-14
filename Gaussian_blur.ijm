/* This will add a gaussian blur to all the open movies in Fiji*/

while (nImages > 0) {

	fileName = getInfo("image.filename") ; 
		//saves image name for future use
		dotIndex = indexOf(fileName, ".");  
		//this and the following line get the file name without the extension
		fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
		//this and the above line get the file name without the extension
		newFileName = fileNameWithoutExtension + "gBlur02-0.tif" ;
	
	run("Gaussian Blur...", "sigma=2.0 stack");
	//saveAs("Tiff","/Users/domchom/Desktop/process_folder/test_220301-gaussian-blur/084DCE/test/blur/waves/"+newFileName);
	run("Save");
	close();
}


