// This will add a gaussian blur to all the open movies in Fiji

// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_SEVEN/404DCE_260930_xEct2-atgged_PIPs_SFC/!processed_images/raw_diff_blur/";

// Define the sigma level
sigma = 3.0; // Change this value to adjust the sigma level


while (nImages > 0) {

	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_gauss" + sigma + "-c1.tif" ;
	
	run("Split Channels");
	
	selectImage("C1-" + imageName);
	
	run("Gaussian Blur...", "sigma=3 stack");
	selectImage("C2-" + imageName);
	run("Gaussian Blur...", "sigma=3 stack");
	run("Merge Channels...", "c1=C1-" + imageName + " c2=C2-" + imageName + " create");
	
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
}

