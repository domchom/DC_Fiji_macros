// batch_calculate_wave_speed.ijm
// Measures wave speed from line ROIs drawn on kymographs (x = distance, y = time).
// Speed = |dx * pixel width| / |dy * frame interval|, so the image's pixel size and
// frame interval must be set correctly (Image > Properties).
//
// Usage:  open the kymographs, run. For each image, draw lines along wave fronts,
//         add each to the ROI Manager (T), then click OK.
// Output: a "Wave speeds" table (one row per line) and the per-image mean in the Log.

// ===== PARAMETERS =====
table_name = "Wave speeds";
// ======================

Table.create(table_name);

while (nImages > 0) {
	title = getTitle();
	baseName = getBaseName(title);
	getPixelSize(unit, pixelWidth, pixelHeight);
	frameInterval = Stack.getFrameInterval();
	if (frameInterval == 0) {
		print("Warning: frame interval is 0 for " + title + "; using pixel height instead.");
		frameInterval = pixelHeight;
	}

	roiManager("reset");
	waitForUser("Add lines to the ROI Manager for " + title + ", then click OK.");

	nLines = roiManager("count");
	total = 0;
	for (i = 0; i < nLines; i++) {
		roiManager("select", i);
		getLine(x1, y1, x2, y2, lineWidth);
		if (x1 == -1 || y1 == y2) {
			print(baseName + " line " + (i + 1) + ": skipped (not a line, or horizontal)");
			continue;
		}
		speed = abs(((x2 - x1) * pixelWidth) / ((y2 - y1) * frameInterval));
		total += speed;

		row = Table.size(table_name);
		Table.set("Image", row, baseName, table_name);
		Table.set("Line", row, i + 1, table_name);
		Table.set("Speed (" + unit + "/s)", row, speed, table_name);
	}
	Table.update(table_name);
	if (nLines > 0) print(baseName + ": mean speed = " + (total / nLines) + " " + unit + "/s over " + nLines + " lines");

	close();
}


// ===== HELPERS =====

// Returns the title without its file extension.
function getBaseName(title) {
	dot = lastIndexOf(title, ".");
	if (dot < 0) return title;
	return substring(title, 0, dot);
}
