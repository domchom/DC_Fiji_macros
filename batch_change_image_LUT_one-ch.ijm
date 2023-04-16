while (nImages > 0) {

	//run("Properties...", "unit=micron pixel_width=.574 pixel_height=.574 voxel_depth=0.5" );
	Stack.setChannel(1);
	run("Grays");
	run("Enhance Contrast", "saturated=0.35");
	run("Save");
	close();
	
					}