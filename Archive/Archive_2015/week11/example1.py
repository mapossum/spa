from osgeo import gdal, ogr
import numpy as np

target_ds = gdal.Open(r'C:\data\spa\data\current_land_cover_small.tif')

myarray = np.array(target_ds.GetRasterBand(1).ReadAsArray())


print myarray / 10.0

print np.min(myarray)

newarray = np.where(myarray == 20, 30, myarray)
print newarray
