//This script takes a group of images that are already opened in Fiji
// and then adds noise based on the "Add Specified Noise..." command
// it then saves it to a specified path


while (nImages > 0) {

	fileName = getInfo("image.filename") ; 
		//saves image name for future use
		dotIndex = indexOf(fileName, ".");  
		//this and the following line get the file name without the extension
		fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
		//this and the above line get the file name without the extension
		newFileName = fileNameWithoutExtension + "noise0.tif" ;
	
	run("Add Specified Noise...", "stack standard=0");
	saveAs("Tiff","/Users/domchom/Desktop/process_folder/test_220301-add-noise-waves/"+newFileName);
	close();
}
