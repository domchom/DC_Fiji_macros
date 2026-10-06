// Duplicate each ROI in the ROI Manager across the full stack and save as TIFF.
// Run with your hyperstack as the active image and ROIs loaded in the ROI Manager.
// ----- edit this -----
outDir = "/Volumes/DOM_SEVEN/371DCE_260624_embryos-fix-Ect2-WTvWA/diseect_scope/frames1to134_single-cells/";// must end with a slash
group = "null";
// ---------------------
setBatchMode(true);
srcID = getImageID();
srcTitle = getTitle();
n = roiManager("count");
if (n == 0) exit("No ROIs in the ROI Manager.");
File.makeDirectory(outDir);   // no-op if it already exists
for (i = 0; i < n; i++) {
    outPath = outDir + group + "-" + i + ".tif";
    if (File.exists(outPath)) {
        print("Skipping (already exists): " + outPath);
        continue;
    }
    selectImage(srcID);
    roiManager("select", i);
    // ROI name becomes the filename; fall back to an index if unnamed
    name = Roi.getName;
    if (name == "" || name == "0") name = "cell_" + IJ.pad(i+1, 3);
    // "duplicate" keeps the full stack/hyperstack; omit it for current frame only
    run("Duplicate...", "title=" + name + " duplicate");
    saveAs("Tiff", outPath);
    close();
}
selectImage(srcID);
setBatchMode(false);
print("Done. Saved crops to " + outDir);