// Blind furrow-timing analysis for single-cell TIFFs.
// Presents cells in randomized order, hides identity, records start/end frame,
// computes the frame difference, and writes a key CSV + a score CSV.
// Run with no image open; ROIs/active image not required.
// ----- edit this -----
inDir  = "/Volumes/DOM_SEVEN/371DCE_260624_embryos-fix-Ect2-WTvWA/diseect_scope/frames1to134_single-cells copy/";
outDir = inDir;          // where the CSVs are written; must end with a slash
seed   = 69;             // KEEP CONSTANT for a given study so order/resume stay consistent
// ---------------------

if (!endsWith(inDir, "/"))  inDir  = inDir + "/";
if (!endsWith(outDir, "/")) outDir = outDir + "/";
keyPath   = outDir + "blind_key.csv";
scorePath = outDir + "furrow_scores.csv";
File.makeDirectory(outDir);

// ---- gather TIFFs ----
raw = getFileList(inDir);
files = newArray(0);
for (i = 0; i < raw.length; i++) {
    lc = toLowerCase(raw[i]);
    if (endsWith(lc, ".tif") || endsWith(lc, ".tiff"))
        files = Array.concat(files, raw[i]);
}
if (files.length == 0) exit("No TIFF files found in:\n" + inDir);

// ---- randomize order (Fisher-Yates, deterministic via seed) ----
random("seed", seed);
order = Array.getSequence(files.length);
for (i = files.length - 1; i > 0; i--) {
    j = floor(random() * (i + 1));
    tmp = order[i]; order[i] = order[j]; order[j] = tmp;
}

// ---- resume support: skip codes already in the score file ----
done = newArray(0);
if (File.exists(scorePath)) {
    lines = split(File.openAsString(scorePath), "\n");
    for (i = 1; i < lines.length; i++) {           // skip header
        c = split(lines[i], ",");
        if (c.length > 0 && c[0] != "") done = Array.concat(done, c[0]);
    }
}

// ---- headers if new ----
if (!File.exists(keyPath))   File.append("blind_code,filename,group", keyPath);
if (!File.exists(scorePath)) File.append("blind_code,start_frame,end_frame,difference,exclude,notes", scorePath);

setBatchMode(false);
total = files.length;

for (k = 0; k < total; k++) {
    code = "cell_" + IJ.pad(k + 1, 3);
    if (inArray(done, code)) {
        print("Skipping (already scored): " + code);
        continue;
    }

    fname = files[order[k]];
    dash  = indexOf(fname, "-");
    group = "unknown";
    if (dash > 0) group = substring(fname, 0, dash);

    open(inDir + fname);
    run("In [+]");
    run("In [+]");
    run("In [+]");
    run("In [+]"); // make the window larger
    rename(code);                                  // hide identity in title bar
    Stack.getDimensions(w, h, ch, sl, fr);
    nFrames = sl; if (fr > sl) nFrames = fr;

    // non-blocking: you can scrub the stack while this is open
    Dialog.createNonBlocking("Blind furrow timing  (" + (k+1) + " / " + total + ")");
    Dialog.addMessage("Code: " + code + "\nScrub the slider to the frames, then enter them below.");
    Dialog.addNumber("Start frame (furrow onset)", 1);
    Dialog.addNumber("End frame (furrow complete)", nFrames);
    Dialog.addCheckbox("Exclude / no furrow", false);
    Dialog.addString("Notes", "", 20);
    Dialog.show();

    start = Dialog.getNumber();
    end   = Dialog.getNumber();
    excl  = Dialog.getCheckbox();
    notes = Dialog.getString();

    diffStr = "" + (end - start);
    exclStr = "0";
    if (excl) { exclStr = "1"; diffStr = ""; }

    notes = replace(notes, ",", ";");
    notes = replace(notes, "\n", " ");

    File.append(code + "," + fname + "," + group, keyPath);
    File.append(code + "," + start + "," + end + "," + diffStr + "," + exclStr + "," + notes, scorePath);
    print(code + ": start=" + start + " end=" + end + " diff=" + diffStr);

    close();
}

print("Done. " + total + " cells.");
print("Key:    " + keyPath);
print("Scores: " + scorePath);
print("Join on 'blind_code' to un-blind.");

function inArray(arr, val) {
    for (i = 0; i < arr.length; i++) if (arr[i] == val) return 1;
    return 0;
}