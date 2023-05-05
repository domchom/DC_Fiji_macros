while (nImages > 0) {

	//run("Properties...", "unit=micron pixel_width=0.385 pixel_height=0.385 voxel_depth=0.5 frame=5");
	Stack.setDisplayMode("composite");
	Stack.setChannel(1);
	run("Magenta");
	resetMinAndMax();
	Stack.setChannel(2);
	run("Green");
	resetMinAndMax();
	run("Save");
	close();
	
					}