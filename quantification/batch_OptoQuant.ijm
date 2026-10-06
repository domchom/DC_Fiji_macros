// batch_OptoQuant.ijm
// Quick optogenetic activation readout: for every open movie and every channel,
// the mean intensity inside one ROI at post_frame divided by the mean at pre_frame.
//
// Usage:  open the movies, run. Draw the activation ROI on the first image and
//         click OK. The same ROI is used for all images.
// Output: an "Opto quant" table with one row per image and one ratio column per channel.

// ===== PARAMETERS =====
pre_frame  = 5;   // last frame before activation
post_frame = 6;   // first frame after activation
table_name = "Opto quant";
// ======================

roiManager("reset");
waitForUser("Draw the opto activation ROI, then click OK.");
if (selectionType() == -1) exit("No ROI selected.");
roiManager("Add");

Table.create(table_name);

while (nImages > 0) {
	baseName = getBaseName(getTitle());
	getDimensions(w, h, nCh, s, f);

	row = Table.size(table_name);
	Table.set("Image", row, baseName, table_name);
	roiManager("select", 0);
	for (c = 1; c <= nCh; c++) {
		ratio = meanAt(c, post_frame) / meanAt(c, pre_frame);
		Table.set("C" + c + " post:pre", row, ratio, table_name);
		print(baseName + " C" + c + " post:pre = " + ratio);
	}
	Table.update(table_name);

	close();
}

// Returns the mean inside the current selection for channel c at frame t.
function meanAt(c, t) {
	if (Stack.isHyperstack) Stack.setPosition(c, 1, t);
	else setSlice(t);
	getStatistics(area, mean);
	return mean;
}


// ===== HELPERS =====

// Returns the title without its file extension.
function getBaseName(title) {
	dot = lastIndexOf(title, ".");
	if (dot < 0) return title;
	return substring(title, 0, dot);
}
