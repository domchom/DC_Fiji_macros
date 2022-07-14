
while (nImages > 0) {

	//run("Properties...", "unit=micron pixel_width=0.385 pixel_height=0.385 voxel_depth=0.5 frame=5");
	Stack.setDisplayMode("composite");
	Stack.setChannel(1);
	run("Magenta");
	run("Enhance Contrast", "saturated=0.35");
	Stack.setChannel(2);
	run("Green");
	run("Enhance Contrast", "saturated=0.35");
	run("Save");
	close();
	
					}