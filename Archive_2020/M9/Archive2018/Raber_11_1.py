from arcpy.sa import *
from arcpy import env
import arcpy
env.overwriteOutput = True

env.workspace = r"C:\temp\spaLab\week10\climatedata.gdb"

rasters = arcpy.ListRasters("temp*")

listofArrays = []
for raster in rasters:
    print raster
    #convert raster into numpy array

    #store numpy array in list

#Build eval statemnt
x = range(0,len(listofArrays))
statement = "listofArrays[" + "] + listofArrays[".join(map(str, x)) + "]"

#eval statement to add up values in array
outputArray = eval(statement)

#divide outputArry by 12 to get new anwser array


#convert answer array using NumPyArrayToRaster

#save to file


