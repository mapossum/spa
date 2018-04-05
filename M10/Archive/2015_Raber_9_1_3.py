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


outCellStatistics = CellStatistics(datasets,"MEAN")

outCellStatistics.save("mean_cs_prec")

t2 = datetime.datetime.now()

print t2 - t1
