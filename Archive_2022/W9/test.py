
import arcpy

#Set workspace
ws = r'C:\temp\Ex 10'
arcpy.env.workspace = ws

#Create variables
outraster = arcpy.sa.Slope('elevation')

outraster.save('slope')
#In working with rasters, it is common to keep most of the intermediate raster datasets in memory as raster objects, 
#and save only the final raster dataset of interest.
