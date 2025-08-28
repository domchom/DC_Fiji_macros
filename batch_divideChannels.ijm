// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

//ensure you have the correct number of channels
Channels_to_divide = 1; // for two channels
//Channels_to_divide - newArray(1,2,3); //for more than two channels
what_to_divide_by = 2;

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_c" + what_to_divide_by + "-normalized.tif" ;

	
	run("Split Channels");
	
	results = newArray(channels - 1);
	idx = 0;
	num_of_loops = channels;
	
	if (channels == 2) {
		imageCalculator("Divide create stack", "C" + Channels_to_divide + "-" + fileName, "C" + what_to_divide_by + "-" + fileName);
		saveAs("Tiff", output_folder_path + newFileName);
		close();
		close();
		close();
		}
	else {
		for (c = 1; c <= num_of_loops; c++) {
			if (c != what_to_divide_by) {
				imageCalculator("Divide create stack", "C" + Channels_to_divide[idx] + "-" + fileName, "C" + what_to_divide_by + "-" + fileName);
				rename("new_C" + c);
				results[idx] = "new_C" + c;
				idx++;
			}
		}
		if (channels == 3) {
			run("Merge Channels...", "c1=" + results[0] + " c2=" + results[1] + " create");
			saveAs("Tiff", output_folder_path + newFileName);
			close();
			close();
			close();
			close();
		}
		if (channels == 4) {
			run("Merge Channels...", "c1=" + results[0] + " c2=" + results[1] + " c3=" + results[2] + " create");
			saveAs("Tiff", output_folder_path + newFileName);
			close();
			close();
			close();
			close();
			close();
		}
	}
}