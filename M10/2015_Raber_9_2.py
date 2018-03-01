import arcpy
from arcpy.sa import *
import numpy
import datetime

arcpy.CheckOutExtension("Spatial")

t1 = datetime.datetime.now()
arcpy.env.workspace = r"C:\temp\week10data"
arcpy.env.extent = r"C:\temp\week10data\tydixton_watershed.shp"

# Print to the Interactive window all the feature datasets in the
#   workspace that start with the letter prec.
datasets = arcpy.ListFeatureClasses("risk*")

c = 0
for dataset in datasets:
    print dataset
    c = c + 1
    ed = EucDistance(dataset, 1000)
    ed.save(dataset.replace(".shp", ".img"))


t2 = datetime.datetime.now()

print t2 - t1
