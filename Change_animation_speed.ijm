//This script changes the animation speed of all movies already opened
//in Fiji and saves them


while (nImages > 0) {

	fileName = getInfo("image.filename") ; 
	//saves image name for future use
	dotIndex = indexOf(fileName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	//this and the above line get the file name without the extension

	selectWindow(fileName);
	run("Animation Options...", "speed=30");
	run("Save");
	close();


		}