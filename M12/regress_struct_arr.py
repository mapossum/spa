from scipy import stats
import numpy as np
import arcpy

input = r"C:\temp\elevClim.gdb\sample_points"
arr = arcpy.da.FeatureClassToNumPyArray(input, ('OID', 'temp', 'elevation'))
print type(arr)
print arr["elevation"]

slope, intercept, r_value, p_value, std_err = stats.linregress(arr["elevation"],arr["temp"])
# To get coefficient of determination (r_squared)

print r_value**2, slope, intercept

pred = (arr["elevation"] * slope) + intercept
res = pred - arr["temp"]
arr["temp"] = res

arr.dtype.names = ("OID", "res", "delev")
print res

arcpy.da.ExtendTable(input, 'OID', arr, "OID")



