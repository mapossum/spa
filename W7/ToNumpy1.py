import arcpy
import numpy as np

table = r'C:\Users\George\courses\spa\M6\Project\Week6_SPA\Week6_SPA.gdb\Tornados_Since_1970'
  
sr = arcpy.SpatialReference(4326)
narray = arcpy.da.FeatureClassToNumPyArray(table, '*', "mag > 1 ", sr)
overallmean = np.mean(narray["mag"])
overallstd = np.std(narray["mag"])
print(overallstd)
for year in range(1970,2018):
    narray = arcpy.da.FeatureClassToNumPyArray(table, '*', "mag > 1 and yr = {}".format(year), sr)
    print(year, np.mean(narray["mag"]), np.mean(narray["mag"]) - overallmean)


