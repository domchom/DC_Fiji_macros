//This macro swaps channel 1 and channel 2 in multi-channel movies

// Define the folder where processed images will be saved
output_folder_path = "/Volumes/DOM_SEVEN/!Ect2-FL-tagged-waves-vs-PIPs/!combined/ch1_PIPs_Ch2-Ect2/";

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getTitle();
	//gets and saves the file name for later
	
	title = getTitle();
	dotIndex = lastIndexOf(title, ".");
	if (dotIndex < 0) dotIndex = lengthOf(title);
	fileNameWithoutExtension = substring(title, 0, dotIndex);
	newFileName = fileNameWithoutExtension + "_swapped.tif" ;

	if (channels == 2) {
		run("Arrange Channels...", "new=21");
	} //swaps ch1 and ch2
	
	if (channels == 3) {
		run("Arrange Channels...", "new=213");
	} //swaps ch1 and ch2, keeps ch3
	
	if (channels == 4) {
		run("Arrange Channels...", "new=2134");
	} //swaps ch1 and ch2, keeps ch3 and ch4
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
	if (isOpen(fileName)) {
		selectWindow(fileName);	
		close();
	} //closes the original if it is still open
}