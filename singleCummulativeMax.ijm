setBatchMode(true);
original = getTitle();
run("Duplicate...", "title=work duplicate");
run("Split Channels");

channels = newArray("C1-work", "C2-work");
for (c = 0; c < channels.length; c++) {
    selectWindow(channels[c]);
    n = nSlices;
    for (i = 2; i <= n; i++) {
        selectWindow(channels[c]);
        setSlice(i - 1);
        run("Duplicate...", "title=prev");
        selectWindow(channels[c]);
        setSlice(i);
        imageCalculator("Max", channels[c], "prev");
        close("prev");
    }
}

run("Merge Channels...", "c1=C1-work c2=C2-work create");
rename(original + "_CumulativeMax");
Stack.setSlice(1);
setBatchMode("exit and display");