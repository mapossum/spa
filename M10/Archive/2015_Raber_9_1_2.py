import arcpy
from arcpy.sa import *
import numpy
import datetime

arcpy.CheckOutExtension("Spatial")

t1 = datetime.datetime.now()
arcpy.env.workspace = r"C:\temp\week10data\data\worldwidedata.gdb"

# Print to the Interactive window all the feature datasets in the
#   workspace that start with the letter prec.
datasets = arcpy.ListDatasets("prec*")


allRasters = []
for dataset in datasets:
    allRasters.append("Raster(r'" + dataset + "')")

print "(" + " + ".join(allRasters) + ") / " + str(len(datasets))
s = eval("(" + " + ".join(allRasters) + ") / " + str(len(datasets)))

s.save("mean_precip")


t2 = datetime.datetime.now()

print t2 - t1
