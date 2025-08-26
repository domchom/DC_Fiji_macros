// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/!IT-Rho/!low-RGA/no-RGA/!combined/square/rotate/";

function findmin(a, b){
	if (a > b) {
		return b
	};
	else {
		return a
	};
}

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_div-by-sum" + ".tif" ;
	
	ori_width = floor(getWidth());
	ori_height = floor(getHeight());
	// Calculate the top-left corner coordinates for the square ROI
	size = findmin(ori_width,ori_height);

	run("Split Channels");
	selectWindow("C2-"+fileName);
	run("Rotate 90 Degrees Right");
	
	// Create the square ROI
	makeRectangle(0, 0, size, size);
	
	run("Crop");
	rename("c2");
	
	selectWindow("C1-"+fileName);
	
	// Create the square ROI
	makeRectangle(0, 0, size, size);
	run("Crop");
	rename("c1");
	
	run("Merge Channels...", "c1=c1 c2=c2 create");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
}
