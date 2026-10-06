#@ DatasetIOService dio
#@ OpService ops
#@ UIService ui
#@ Integer gray_levels(label="Gray Levels:", value=0)
#@ Integer dist(label="Distance:", value=0)
#@ File (label="Input directory", style="directory") in_dir
#@ String (label="File extension", value=".tif") ext

import os
from net.imagej.ops.image.cooccurrenceMatrix import MatrixOrientation2D
from net.imglib2.type.numeric.real import DoubleType
from org.scijava.table import DefaultGenericTable

# create orientation list
orientations = [
    MatrixOrientation2D.ANTIDIAGONAL,
    MatrixOrientation2D.DIAGONAL,
    MatrixOrientation2D.HORIZONTAL,
    MatrixOrientation2D.VERTICAL
]

def open_images(path):
    """
    Open images in a given directory/path with the specified extension.

    :param path: Input directory string.
    :return: A dict of net.imagej.Dataset.
    """
    # extract the image paths to a list
    paths = {}
    data_dir = in_dir.getAbsolutePath()
    for root, dirs, file_names in os.walk(data_dir):
        file_names.sort()
        for name in file_names:
            # check for file extension
            if not name.endswith(ext):
                continue
            paths[name] = (os.path.join(root, name))

    # open image image and save as a list
    images = {}
    for k, v in paths.items():
        images[k] = dio.open(v)
    
    return images


def run_glcm(img, gray_levels, dist, angle):
    """
    Compute the correlation and difference variance GLCM textures from an image.

    :param img: An input ImgPlus
    :param gray_levels: Number of gray levels
    :param dist: Distance in pixels
    :param angle: MatrixOrientation2D angle
    :return: A tuple of floats: (correlation, difference variance)
    """
    # compute correlation and difference variance
    corr = ops.haralick().correlation(img, gray_levels, dist, angle)
    diff = ops.haralick().differenceVariance(img, gray_levels, dist, angle)
    cluster_var = ops.haralick().clusterShade(img, gray_levels, dist, angle)
    homogeneous = ops.haralick().textureHomogeneity(img, gray_levels, dist, angle)
    IFDM_val = ops.haralick().ifdm(img, gray_levels, dist, angle)

    return (corr, diff, cluster_var, homogeneous, IFDM_val)


def mean(vals):
    """
    Compute the mean of a list of DoubleType.

    :param vals: A list of DoubleType.
    :return: Mean of list of DoubleType.
    """
    total = DoubleType(0.0)
    count = 0
    # get the sum of vals
    for v in vals:
        total = ops.math().add(total, v)
        count += 1
    # compute the mean
    if count == 0:
        return DoubleType(0.0) # avoid zero division
    else:
        return ops.math().divide(total, DoubleType(count))


def process_images(images, gray_levels, dist):
    """
    Process a dict of net.imagej.Dataset images with GLCM
    correlation and difference variance texture analysis.

    :param images: A dict of net.imagej.Dataset images.
    :param gray_levels: Number of gray levels
    :param dist: Distance in pixels
    :return: A SciJava Table with GLCM results. 
    """
    glcm_mean_results = {}
    for k, v in images.items():
        glcm_angle_results = []
        # compute the correlation and difference variance textures for all orientations
        for angle in orientations:
            glcm_angle_results.append(run_glcm(v, gray_levels, dist, angle))
        # compute the mean of the angle results
        corr_glcm_angle_vals = [x[0] for x in glcm_angle_results]
        diff_glcm_angle_vals = [x[1] for x in glcm_angle_results]
        cluster_glcm_angle_vals = [x[2] for x in glcm_angle_results]
        homogeneous_glcm_angle_vals = [x[3] for x in glcm_angle_results]
        IFDM_glcm_angle_vals = [x[4] for x in glcm_angle_results]
        glcm_mean_results[k] = ((mean(corr_glcm_angle_vals),
                                 mean(diff_glcm_angle_vals), 
                                 mean(cluster_glcm_angle_vals), 
                                 mean(homogeneous_glcm_angle_vals),
                                 mean(IFDM_glcm_angle_vals)
                                 ))

    columns = ["name", "corr", "diff", "cluster", "homogeneous", "IFDM"]

    # create scijava table and populate results
    table = DefaultGenericTable(len(columns), len(glcm_mean_results))
    for i, col in enumerate(columns):
        table.setColumnHeader(i, col)

    row = 0 # counter
    for k, v in glcm_mean_results.items():
        if row <= len(glcm_mean_results):
            table.set("name", row, k)
            table.set("corr", row, v[0])
            table.set("diff", row, v[1])
            table.set("cluster", row, v[2])
            table.set("homogeneous", row, v[3])
            table.set("IFDM", row, v[4])
            row += 1
        else:
            break

    return table

# open images as a dict
images = open_images(in_dir)

# run GLCM analysis on image dict
rt = process_images(images, gray_levels, dist)

# display table
ui.show(rt)