//This script changes the animation speed of all movies already opened in Fiji and saves them

animation_speed = 30;

while (nImages > 0) {

	run("Animation Options...", "speed=" + animation_speed);
	run("Save");
	close();


		}