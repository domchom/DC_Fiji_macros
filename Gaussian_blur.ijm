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
	saveAs("Tiff","/Volumes/DOM_LS/125DCE_230224_Rho-IT-waves_SFC/processed/crop_trimmer_10-x_diff12_gblur2.0/"+newFileName);
	//run("Save");
	close();
}


