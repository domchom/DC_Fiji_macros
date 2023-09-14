// Get the active image (assumes a stack is open)
run("32-bit");
run("Remove Outliers...", "radius=3 threshold=100 which=Bright stack");
getDimensions(width, height, channels, slices, frames);

// Find the global minimum and maximum pixel values
for (frame = 1; frame <= frames; frame++) {
	run("Duplicate...", " ");

	run("Measure", "mean");
	frameMean = getResult("Mean");
	frameMin = getResult("Min");
	frameMax = getResult("Max");
	
	if (frame == 1) {
		newmin = frameMin;
		newmax = frameMax;
	}

	close() ;

	// Divide pixel values by the mean intensity
	run("Subtract...", "value=" + frameMin + " slice");
	run("Multiply...", "value=" + (newmax - newmin) / (frameMax - frameMin) + " slice");
	//run("Divide...", "value=" + (frameMax - frameMin) + " slice");
	
    run("Next Slice [>]");
}