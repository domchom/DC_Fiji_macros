while (nImages > 0) {

	//run("Properties...", "unit=micron pixel_width=0.385 pixel_height=0.385 voxel_depth=0.5 frame=5");
	run("Properties...", "channels=2 slices=1 frames=1 pixel_width=0.2661449 pixel_height=1.0000000 voxel_depth=1.0000000 frame=3.75");
	run("Save");
	close();
	
					}