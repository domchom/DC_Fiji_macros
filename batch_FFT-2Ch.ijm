// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/177DCE_tagged-Ect2/LS/raw_div-sum/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_FFT_correct" + ".tif" ;
	
	run("Split Channels");
	selectWindow("C1-"+fileName);
	rename("C1");
	run("FFT");
	waitForUser("Select contaminants for " + fileName);
	

	run("Create Mask");
	rename("MaskC1");
	run("Invert");
	run("Gaussian Blur...", "sigma=2");
	selectWindow("C1");
	run("Custom Filter...", "filter=MaskC1");
	
	selectWindow("C2-"+fileName);
	rename("C2");
	run("FFT");
	waitForUser("Select contaminants for " + fileName);
	

	run("Create Mask");
	rename("MaskC2");
	run("Invert");
	run("Gaussian Blur...", "sigma=2");
	selectWindow("C2");
	run("Custom Filter...", "filter=MaskC2");
	
	run("Merge Channels...", "c1=C1 c2=C2 create");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
	close();
	close();
	close();
}
