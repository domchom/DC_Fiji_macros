// Define the folder where processed images will be saved
output_folder_path = "/Volumes/T7/!Rho-IT/180DCE_200v1000_Rho-IT_waves_LS/processed/raw_3dReg/";

while (nImages > 0) {

	fileName = getInfo("image.filename") ; 
	path = getDirectory("image") ;
	//saves path that the image is saved to
	dotIndex = indexOf(fileName, ".");  
	fileNameWithoutExtension = substring(fileName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_reg.tif" ;

	run("Re-order Hyperstack ...", "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]");
	run("PoorMan3DReg ", "transformation=Translation number=2 projection=[Max Intensity]");
	run("Re-order Hyperstack ...", "channels=[Slices (z)] slices=[Channels (c)] frames=[Frames (t)]");

	Stack.setDisplayMode("composite");
	Stack.setChannel(1);
	run("Magenta");
	run("Enhance Contrast", "saturated=0.15");
	Stack.setChannel(2);
	run("Green");
	run("Enhance Contrast", "saturated=0.15");
	
	saveAs("Tiff", output_folder_path + newFileName);	
	close();
	
					}