//saves the frames as specified by the user

while (nImages > 0) {

	fileName = getInfo("image.filename") ; 
		//saves image name for future use
		dotIndex = indexOf(fileName, ".");  
		//this and the following line get the file name without the extension
		fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
		//this and the above line get the file name without the extension
		newFileName = fileNameWithoutExtension + "_frames1-15.tif" ;
		run("Duplicate...", "duplicate range=1-15");
		saveAs("Tiff","/Volumes/DOM_THREE/!analysis/006_007_009_018_086_087_xEct2-Chen/short/087DCE/"+newFileName);
		close();
		close();
}
		
