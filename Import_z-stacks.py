# Importing modules and other shit
import os, sys, traceback, shutil, glob
from ij import IJ, WindowManager, ImagePlus
from ij.gui import GenericDialog
from ij.plugin import ImageCalculator
import datetime
import fnmatch

experimentFolder = '/Volumes/DOM_LS/129DCE_230316_Rho-IT-waves-SFC/stacks_scope_folders'

saveFolder = os.path.join(experimentFolder, "processed")
if os.path.isdir(saveFolder) ==True:
	shutil.rmtree(saveFolder)

os.makedirs(saveFolder)

# list_scans gets a list of all scan folders inside the experimentFolder you selected, and saves them as a list called scanList.
def list_scans(experimentFolder):
	scanList = [] # Makes an empty list

	# This section screens out text files and other things that might be in the main experimentFolder, and only makes a list of the actual scan directories
	for File in sorted(os.listdir(experimentFolder)):
		dirpath = os.path.join(experimentFolder, File) # Makes a complete path to the file
		if os.path.isdir(dirpath): # If the dirpath is a directory, print it and add it to scanList. If it's a file, do not add it.
			print "dirpath is " + dirpath
			scanList.append(dirpath)
	
	#scanList.remove(saveFolder) #removes the saveFolder from the list 
	return scanList # Returns scanList to run_it()

# Make_hyperstack uses Bio-formats importer to import a hyperstack from an initiator file
def make_hyperstack(basename, scan): # basename is defined in run_it() and is the name of the scan (not the full path)

	# Defines an "initator file" to give bioformats importer, and also modifies basename (which has an .oif.files extension) to make the scan name

	print "basename is ", basename # The basename doesn't need to be modified here, because there is no .oif.files suffix to remove (Thanks Bruker!)
	initiatorFileName = basename + "_Cycle00001_Ch?_000001.ome.tif" # Defines the pattern to look for. The Ch? is because if you have one color, it's not always on CH1
	initiatorFilePath = os.path.join(scan, initiatorFileName) # Gets the full path to the initiator file
	print "initiatorFilePath ", initiatorFilePath
	initiatorFilePath = glob.glob(initiatorFilePath) # Looks for the first file in the folder. If there are more than one channel, it makes a list of them.
	initiatorFilePath = initiatorFilePath[0] # Takes the first item in the list. This is the file that will get passed to bioformats importer
	print "Opening file", initiatorFilePath

	IJ.run("Bio-Formats Importer", "open=[" + initiatorFilePath + "] color_mode=Grayscale concatenate_series open_all_series quiet rois_import=[ROI manager] view=Hyperstack stack_order=XYCTZ")
	print "File opened"
	imp = IJ.getImage()
	windowName = imp.getTitle()

	IJ.saveAsTiff(imp, os.path.join(saveFolder,windowName)) #saves to saveFolder

def run_it():
	scanList = list_scans(experimentFolder)
	print "The returned scanList is", len(scanList), "item(s) long"

	for scan in scanList:
		basename = os.path.basename(scan) # get the scan name (basename)

		make_hyperstack(basename, scan) # open the hyperstack
		imp = IJ.getImage() # select the open image
		channels = imp.getNChannels() #gets the number of channels
		print "The number of channels is", channels
		
		IJ.run("Close All")

		IJ.freeMemory() # runs garbage collector

run_it()
print "Done with script"
