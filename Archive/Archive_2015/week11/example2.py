from osgeo import gdal, ogr
import numpy as np

target_ds = gdal.Open(r'C:\data\spa\data\current_land_cover_small.tif')
precip_ds = gdal.Open(r'C:\data\spa\data\prec_6_small_2.tif')

print target_ds.GetGeoTransform()


lcArray = np.array(target_ds.GetRasterBand(1).ReadAsArray())
pArray = np.array(precip_ds.GetRasterBand(1).ReadAsArray())

pinePrecipArray = pArray[np.where(lcArray == 4)]
shrubPrecipArray = pArray[np.where(lcArray == 13)]


print np.mean(pinePrecipArray)
print np.mean(shrubPrecipArray)

print np.size(lcArray)
