// Define the folder where processed images will be saved
output_folder_path = "/Users/domchom/Desktop/test/";

channel_to_rotate = 2;

function findmin(a, b){
	if (a > b) {
		return b
	};
	else {
		return a
	};
}

while (nImages > 0) {
	getDimensions(width, height, channels, slices, frames) ;		
	//gets and saves the movie dimensions for later use
	fileName = getInfo("image.title"); 
	//gets and saves the file name for later
	
	imageName = getInfo("image.filename") ; 
	dotIndex = indexOf(imageName, ".");  
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	newFileName = fileNameWithoutExtension + "_Ch" + channel_to_rotate + "rotated.tif";
	
	ori_width = floor(getWidth());
	ori_height = floor(getHeight());
	// Calculate the top-left corner coordinates for the square ROI
	size = findmin(ori_width,ori_height);

	run("Split Channels");
	selectWindow("C" + channel_to_rotate + "-" + fileName);
	run("Rotate 90 Degrees Right");
	
	// Create the square ROI
	makeRectangle(0, 0, size, size);
	
	run("Crop");
	
	//find the unused channels
	if (channels == 2) {
		unused = newArray("");
	}
	if (channels == 3) {
		unused = newArray("", "");
	}
	if (channels == 4) {
		unused = newArray("", "", "", "");
	}
	
	idx = 0;
	for (c = 1; c <= channels; c++) {
        if (c != channel_to_rotate) {
            unused[idx] = "C" + c + "-" + imageName;
            selectWindow("C" + c + "-" + imageName);
            // Create the square ROI
			makeRectangle(0, 0, size, size);
			run("Crop");
            idx++;
        }
	}
	
	if (channels == 2) {
		run("Merge Channels...", "c1=C1-" + fileName + " c2=C2-" + fileName + " create");
	}
	if (channels == 3) {
		run("Merge Channels...", "c1=C1-" + fileName + " c2=C2-" + fileName + " c3=C3-" + fileName + " create");
	}
	if (channels == 4) {
		run("Merge Channels...", "c1=C1-" + fileName + " c2=C2-" + fileName + " c3=C3-" + fileName + " c4=C4-" + fileName + " create");
	}
	
	saveAs("Tiff", output_folder_path + newFileName);
	close();
}
