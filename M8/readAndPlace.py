import pandas as pd
import arcpy
import numpy as np

fdata = r"C:\temp\Week7.gdb\Hexagons_USA_Cont"
arr = arcpy.da.FeatureClassToNumPyArray(fdata, "*")
print(type(arr))

#eqsdata = pd.DataFrame.from_records(arr)

#print(eqsdata)


from arcgis.features import GeoAccessor as SDF

a = SDF.from_featureclass(fdata)

print(a)

