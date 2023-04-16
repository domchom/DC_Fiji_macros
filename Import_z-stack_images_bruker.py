'''This code currently only works for Bruker file types'''

import os
import glob
import shutil
import datetime
import traceback
from ij import IJ, WindowManager

input_folder_path = '/Users/domchom/Desktop/230403/'

def list_scans(input_folder_path):
    """
    Returns a list of all scan folders inside the experiment folder.
    """
    scan_list = [] # Makes an empty list
    for filename in sorted(os.listdir(input_folder_path)):
        filepath = os.path.join(input_folder_path, filename)
        if os.path.isdir(filepath): # If the file is a directory, add it to the list
            scan_list.append(filepath)
    return scan_list

def load_initiator_file(scan, basename):
    """
    Returns the path to the initiator file for the given scan.
    """
    initiator_file_name = basename + "_Cycle00001_Ch?_000001.ome.tif"
    initiator_file_path = glob.glob(os.path.join(scan, initiator_file_name))
    if not initiator_file_path:
        raise TypeError("No initiator file found for " + basename)
    initiator_file_path = initiator_file_path[0]
    return initiator_file_path

def make_hyperstack(initiator_file_path, save_folder):
    """
    Imports a hyperstack from the given initiator file and saves it to the specified folder.
    """
    IJ.run("Bio-Formats Importer", "open=[" + initiator_file_path + "] color_mode=Grayscale concatenate_series open_all_series quiet rois_import=[ROI manager] view=Hyperstack stack_order=XYCTZ")
    imp = IJ.getImage()
    windowName = imp.getTitle()
    IJ.saveAsTiff(imp, os.path.join(save_folder,windowName))

def run_it():
    """
    Processes all scan folders in the input folder.
    """
    # Create an error log file
    error_file_path = os.path.join(input_folder_path, "errorFile.txt")
    now = datetime.datetime.now()
    with open(error_file_path, "w") as error_file:
        error_file.write("\n" + now.strftime("%Y-%m-%d %H:%M") + "\n")
        error_file.write("#### import z-stacks ####" + "\n")

    # Finds all image names and saves them to scan_list
    scan_list = list_scans(input_folder_path)
    print "The returned scan list is", len(scan_list), "item(s) long"

    # Create output directory for processed images
    save_folder = os.path.join(input_folder_path, "processed")
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    for scan in scan_list:
        try:
            basename = os.path.basename(scan)
            print "Processing " + basename
            with open(error_file_path, "a") as error_file:
                error_file.write("\n \n -- Processing " + basename + " --" + "\n")

            # Load initiator file and create hyperstack
            initiator_file_path = load_initiator_file(scan, basename)
            make_hyperstack(initiator_file_path, save_folder)
            
            # Close all open windows and free memory
            IJ.run("Close All")
            IJ.freeMemory() 

        except Exception as e:
            print "Error with ", basename, "continuing on..."
            with open(error_file_path, "a") as error_file:
                error_file.write("\n" + now.strftime("%Y-%m-%d %H:%M") + "\n")
                error_file.write("Error with " + basename + "\n" + "\n")
                traceback.print_exc(file=error_file)
            
            # Close all open windows and free memory
            IJ.run("Close All")
            IJ.freeMemory()
            continue
    
    # Move all existing folders into a new folder
    scope_folder = os.path.join(input_folder_path, 'scope_folders')
    if not os.path.exists(scope_folder):
        os.mkdir(scope_folder)
    for folder in os.listdir(input_folder_path):
        folder_path = os.path.join(input_folder_path, folder)
        if os.path.isdir(folder_path) and folder not in [scope_folder, 'processed']:
            shutil.move(folder_path, scope_folder)

    # Close the error log file
    with open(error_file_path, "a") as error_file:
        error_file.write("\nDone with script.\n")
        
    print "Done with script"

run_it()

