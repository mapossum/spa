from osgeo import gdal, ogr
import numpy as np

# Define pixel_size and NoData value of new raster
pixel_size = 25
NoData_value = -9999

# Filename of input OGR file
vector_fn = r'C:\data\spa\risk_ag_sugarcane.shp'

# Filename of the raster Tiff that will be created
raster_fn = 'test.tif'
raster2_fn = 'test2.tif'
raster2_fn = 'test3.tif'

# Open the data source and read in the extent
source_ds = ogr.Open(vector_fn)
source_layer = source_ds.GetLayer()
x_min, x_max, y_min, y_max = source_layer.GetExtent()

# Create the destination data source
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)
target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
band = target_ds.GetRasterBand(1)
band.SetNoDataValue(NoData_value)

# Rasterize
gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])

#Find Distance
target2_ds = gdal.GetDriverByName('GTiff').Create(raster2_fn, x_res, y_res, 1, gdal.GDT_Int16)
target2_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

srcband = target_ds.GetRasterBand(1)
dstband = target2_ds.GetRasterBand(1)
gdal.ComputeProximity( srcband, dstband)

#Convert to Array
myarray = np.array(target2_ds.GetRasterBand(1).ReadAsArray())

#Convert from Array
target3_ds = gdal.GetDriverByName('GTiff').Create(raster2_fn, x_res, y_res, 1, gdal.GDT_CFloat64)
target3_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

#You can do math operations
newarray = myarray[:]
parray = (myarray + newarray) / 3.0


#The where operator works like CON
newarray = np.where(myarray < 20, myarray, 0)

print myarray
print newarray
print parray
#thing demonstrates zonal
print np.mean(parray[np.where(myarray < 20)])

#write into Array
outBand = target3_ds.GetRasterBand(1)
outBand.WriteArray(parray)

#outBand.FlushCache()

source_ds = None
target_ds = None
target2_ds = None
target3_ds = None






