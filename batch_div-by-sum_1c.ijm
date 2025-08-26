// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/!Ect2-delBRCT/239DCE_241002_xEct2-BRCTdel_SFC/!processed_images/raw_dbs/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_div-by-sum" + ".tif" ;
	
	rename("C1");
	run("Z Project...", "projection=[Sum Slices]");
	imageCalculator("Divide create 32-bit stack", "C1","SUM_C1");
	rename("C1_result");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
	close();
}
