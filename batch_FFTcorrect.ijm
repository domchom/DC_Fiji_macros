// ONLY WORKING FOR 2 CHANNEL FOR NOW

// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Documents/Bement_lab/Meetings_Conferences/!Committee-meetings/260603_sixMonth-meeting/dh-tagged/";

//channels_to_correct = 1;
channels_to_correct = newArray(1,2);
num_ch_to_correct = 2;

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
	
	results = newArray(num_ch_to_correct);
	idx = 0;
	for (c = 1; c <= num_ch_to_correct; c++) {
		selectWindow("C" + channels_to_correct[idx] + "-" + fileName);
		run("FFT");
		waitForUser("Select contaminants for C" + channels_to_correct[idx] + "-" + fileName);
		
		run("Create Mask");
		rename("MaskC" + channels_to_correct[idx]);
		run("Invert");
		run("Gaussian Blur...", "sigma=2");
		selectWindow("C" + channels_to_correct[idx] + "-" + fileName);
		run("Custom Filter...", "filter=MaskC" + channels_to_correct[idx]);
		rename("C" + channels_to_correct[idx]);
		results[idx] = "C" + channels_to_correct[idx];
		idx++;
	}
	
	if (channels == 2) {
		run("Merge Channels...", "c1=C1 c2=C2 create");
	}
	
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	close();
	close();
	close();
	close();
}
