input_folder_path = "/Volumes/T7/181DCE_tagged_Ect2/LS/scope_folders/20231117_134740_181DCE_2xmChEct2dNLS_GFPUtrCH_1500ng_cell9_enface_20min/_projection/";
output_folder_path = "/Volumes/T7/181DCE_tagged_Ect2/LS/processed/";

File.openSequence(input_folder_path, " filter=C01");
rename("C01.tif");
File.openSequence(input_folder_path, " filter=C02");
rename("C02.tif");
run("Merge Channels...", "c1=C01.tif c2=C02.tif create");
run("Re-order Hyperstack ...", "channels=[Channels (c)] slices=[Frames (t)] frames=[Slices (z)]");

image1 = split(input_folder_path,"/");

image = image1[image1.length - 2];

// Save the file in the original folder with a new name
saveAs("Tiff", output_folder_path + image + ".tif");

close();