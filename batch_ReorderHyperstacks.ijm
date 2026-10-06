// Define the folder where processed images will be saved

while (nImages > 0) {
	
	run("Re-order Hyperstack ...", "channels=[Channels (c)] slices=[Frames (t)] frames=[Slices (z)]");
	run("Save");
	close();
					}

