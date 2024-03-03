// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/190DCE_240117_3xGFP-Ect2-PH(PBC)_mCh-Rho-IT_BFP_SFC/processed/div_c1-c2_by_c3/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_c3-normalized" + ".tif" ;

	
	run("Split Channels");
	imageCalculator("Divide create stack", "C1-"+fileName,"C3-"+fileName);
	selectImage("Result of C1-"+fileName);
	rename("new_C1");
	
	imageCalculator("Divide create stack", "C2-"+fileName,"C3-"+fileName);
	selectImage("Result of C2-"+fileName);
	rename("new_C2");
	
	run("Merge Channels...", "c1=[new_C1] c2=[new_C2] create");
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
	close();
	close();

}