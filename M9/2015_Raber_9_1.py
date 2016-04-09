import arcpy
from arcpy.sa import *
import numpy


arcpy.CheckOutExtension("Spatial")

arcpy.env.workspace = r"C:\temp\week10data\data\worldwidedata.gdb"

# Print to the Interactive window all the feature datasets in the
#   workspace that start with the letter prec.
datasets = arcpy.ListDatasets("prec*")


d = datasets.pop(0)
print d, "This is the first one"
for dataset in datasets:
    print dataset, d
    tadd = Plus(dataset, d)
    d = tadd

meanout = d / len(datasets) + 1

d.save("total_prec")
meanout.save("mean_prec")
