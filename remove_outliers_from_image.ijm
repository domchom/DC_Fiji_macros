while (nImages > 0) {

	run("Remove Outliers...", "radius=2 threshold=200 which=Bright stack");
	run("Save");
	close();

}