import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = r""
env.extent = ""
env.overwriteOutput = True



outCon.save()
