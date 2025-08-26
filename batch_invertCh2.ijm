// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/!IT-Rho/!low-RGA/no-RGA/!combined/invert C2/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_div-by-sum" + ".tif" ;
	
	run("Split Channels");
	selectWindow("C2-"+fileName);
	run("Flip Horizontally");
	rename("c2");
	
	selectWindow("C1-"+fileName);
	rename("c1");
	
	run("Merge Channels...", "c1=c1 c2=c2 create");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
}
