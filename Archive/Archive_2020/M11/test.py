# have dimensions of (rows, columns, slices).

import arcpy
import numpy as np
from scipy import stats

#Specify Study Area
studyarea = r'C:\temp\FinalData.gdb\sample1'

#Specify Output Location for Output Raster
outputLapse = r'C:\temp\FinalData.gdb\Lapse1'

#Set up input Rasters
tempRaster = arcpy.Raster(r'C:\temp\FinalData.gdb\USA_elevation_meters')
elevRaster = arcpy.Raster(r'C:\temp\FinalData.gdb\USA_temp_June_ave')

#Set nessessary enviornmental variables
arcpy.env.mask = studyarea
arcpy.env.extent = studyarea

#get a Raster just for the area we need
tempArea = arcpy.sa.Times(tempRaster, 1.0)
elevArea = arcpy.sa.Times(elevRaster, 1.0)

# Convert Raster to numpy array
temparr = arcpy.RasterToNumPyArray(tempArea, nodata_to_value = -9999).flatten() 
elevarr = arcpy.RasterToNumPyArray(elevArea, nodata_to_value = -9999).flatten()

#This gets the indexs of all those areas not no Data
x = np.where(temparr > -9999)

slope, intercept, r_value, p_value, std_err = stats.linregress(temparr[x],elevarr[x])

print(slope, intercept, r_value, p_value, std_err)

#Lets think about what else we need to do.
