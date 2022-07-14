//measures the intensity for a set of open movies. Will have you select an ROI (line format, not a box)
// and then create a kymograph of that line ROI. then will iterate over each row to find the 
// avg intesity over time, and save it to a csv file


titles = getList("image.titles");	// sets titles equal to an array containing all of the image names that are curently open
for (y=0; y<titles.length; y++){    // one trip through the loop for every open image
	selectWindow(titles[y]);		// selects an image
	getDimensions(width, height, channels, slices, frames);

	imageName = getInfo("image.filename") ; 
	//saves image name for future use
	dotIndex = indexOf(imageName, ".");  
	//this and the following line get the file name without the extension
	fileNameWithoutExtension = substring(imageName, 0, dotIndex); 
	//this and the above line get the file name without the extension
	newFileName = fileNameWithoutExtension + "_stats.csv" ;

	
	waitForUser("Select ROI", "Select ROI"); //select the roi for which a kymo graph will be made
	run("Reslice [/]...", "output=1.000 slice_count=1 avoid"); //makes kymograph
	getDimensions(width, height, channels, slices, frames);	//gets the dimensions and set the varible for creating lines
	w = width;
	h = height;

	for (i=0; i<height; i++) { //measures the average intensity for each row of pixels down the kymograph
		makeLine(0,i+1,w,i+1);
		run("Measure");	
	}
	selectWindow("Results");
	saveAs("text","/Users/domchom/Desktop/test-txt/"+newFileName); //saves the results to a specified path as a .csv
	close("Results"); 
	close(); //closes kymograph
	close(); //closes movie
}
	