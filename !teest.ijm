// Define the folder where cropped images will be saved
output_folder_path = "/Volumes/T7/!IT-Rho/!low-RGA/no-RGA/223DCE_240711_IT-Rho_200ng_Ect2-noRGA_SFC/!processed_images/raw_reg_crop/";

while (nImages > 0) {

	fileName = getInfo("image.filename") ; 
	dotIndex = indexOf(fileName, ".");  
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_crop.tif" ;
	
	run("Z Project...", "projection=[Min Intensity]");
	selectWindow("MIN_" + fileName);
	
	run("Z Project...", "projection=[Max Intensity]");	//FOR TWO-CHANNEL DATASETS
	selectWindow("MAX_MIN_" + fileName);				//FOR TWO-CHANNEL DATASETS
	
	setThreshold(1, 65535);
	run("Convert to Mask");
	run("Analyze Particles...", "add");
	selectWindow(fileName);
	roiManager("Select", 0);
	run("Crop");
	run("Select None");
	saveAs("Tiff",output_folder_path+newFileName);
	close();
	
	selectWindow("MIN_" + fileName);
	close();
	
	selectWindow("MAX_MIN_" + fileName); 	//FOR TWO-CHANNEL DATASETS
	close();								//FOR TWO-CHANNEL DATASETS
	
	roiManager("Delete");
	
					}