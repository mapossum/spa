from osgeo import gdal, ogr
import numpy as np

#Open the orginal Dataset
target_ds = gdal.Open(r'C:\data\spa\data\current_land_cover_small.tif')

#get transformation information
geotrans = target_ds.GetGeoTransform()
cols = target_ds.RasterXSize
rows = target_ds.RasterYSize

#create empty dataset
raster_fn = r'C:\data\spa\data\current_land_cover_small_3.tif'
output_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, cols, rows, 1, gdal.GDT_CFloat64)
output_ds.SetGeoTransform(geotrans)

#manipulate data
myarray = np.array(target_ds.GetRasterBand(1).ReadAsArray())


print myarray / 10.0

print np.min(myarray)

newarray = np.where(myarray > 15, 30, myarray)

#write manupulated data out
outBand = output_ds.GetRasterBand(1)
outBand.WriteArray(myarray / 10.0)


output_ds = None
