// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/!Ect2_titration/169_172_174_175_combined/raw_crop/originals/div-by-sum/";

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
	selectWindow("C1-"+fileName);
	rename("C1");
	run("Z Project...", "projection=[Sum Slices]");
	imageCalculator("Divide create 32-bit stack", "C1","SUM_C1");
	rename("C1_result");
	run("16-bit");
	
	selectWindow("C2-"+fileName);
	rename("C2");
	run("Z Project...", "projection=[Sum Slices]");
	imageCalculator("Divide create 32-bit stack", "C2","SUM_C2");
	rename("C2_result");
	run("16-bit");
	
	run("Merge Channels...", "c1=C1_result c2=C2 create");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
	close();
	close();
	close();
}
