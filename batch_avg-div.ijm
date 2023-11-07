// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_FIVE/167DCE/processed/raw_div-avg/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_div-by-avg" + ".tif" ;
	
	run("Split Channels");
	selectWindow("C1-"+fileName);
	rename("C1");
	run("Z Project...", "projection=[Average Intensity]");
	imageCalculator("Divide create 32-bit stack", "C1","AVG_C1");
	rename("C1_result");
	run("16-bit");
	
	selectWindow("C2-"+fileName);
	rename("C2");
	
	run("Merge Channels...", "c1=C1_result c2=C2 create");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
	close();
}
