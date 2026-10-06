// ImageJ/Fiji macro: Remove static pixels from a single-channel, multi-frame stack
// Method: detect pixels with low temporal variation, replace with local median

// --- Parameters (tweak as needed) ---
rangeThresh = 5000;    // min intensity change across frames to be considered "dynamic"
kernelRadius = 1;   // radius for local median replacement (1 = 3x3 neighborhood)

// --- Setup ---
origTitle = getTitle();
run("Duplicate...", "duplicate");
rename("workstack");
run("Re-order Hyperstack ...", "channels=[Channels (c)] slices=[Frames (t)] frames=[Slices (z)]");

// --- Compute per-pixel temporal range ---
run("Z Project...", "projection=[Min Intensity]");
rename("minproj");
selectWindow("workstack");
run("Z Project...", "projection=[Max Intensity]");
rename("maxproj");

imageCalculator("Subtract create", "maxproj","minproj");
rename("rangeimg");

// --- Threshold static pixels ---
setThreshold(0, rangeThresh);
run("Convert to Mask");
rename("static_mask");

//// Optional: clean up mask
//run("Open");   // remove single-pixel specks
//run("Close");  // close tiny holes

// --- Apply correction frame by frame ---
selectWindow("workstack");
Stack.getDimensions(width, height, channels, slices, frames);
for (i = 1; i <= slices; i++) {
	selectWindow("workstack");
	print(i);
    setSlice(i);
    run("Duplicate...", " ");
    rename("tempframe");
    // Median filter to get local background
    run("Median...", "radius="+kernelRadius);
    rename("localmed");
    // Replace masked pixels
    imageCalculator("AND create", "localmed","static_mask");
    rename("repl");
    selectWindow("repl");
    run("Select All"); run("Copy");
    selectWindow("workstack");
    setSlice(i);
    run("Paste");
    close("localmed"); close("repl");
}

// --- Cleanup ---
selectWindow("workstack");
rename(origTitle+"-cleaned");