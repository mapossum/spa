from osgeo import gdal, ogr
import numpy as np
import glob
from scipy import ndimage

# Define pixel_size and NoData value of new raster
pixel_size = 25
NoData_value = -9999

# Filename of input OGR file
watershed_fn = r'C:\data\spa\tydixton_watershed.shp'
vector_fn_list = glob.glob(r"C:\data\spa\risk*.shp")

# Filename of the raster Tiff that will be created
raster_fn = r'C:\data\spa\risk_dataset.tif'
raster2_fn = r'C:\data\spa\risk_distance.tif'

# Open watershed data and read extent
watershed_ds = ogr.Open(watershed_fn)
watershed_layer = watershed_ds.GetLayer()
x_min, x_max, y_min, y_max = watershed_layer.GetExtent()

print watershed_layer.GetExtent()

#looped
arraylist = []

for vector_fn in vector_fn_list:
    # Open the data source
    source_ds = ogr.Open(vector_fn)
    source_layer = source_ds.GetLayer()

    ### Create the destination data source
    x_res = int((x_max - x_min) / pixel_size)
    y_res = int((y_max - y_min) / pixel_size)
    target_ds = gdal.GetDriverByName('GTiff').Create(raster_fn, x_res, y_res, 1, gdal.GDT_Byte)
    target_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))
    band = target_ds.GetRasterBand(1)
    band.SetNoDataValue(NoData_value)

    ##
    ### Rasterize
    gdal.RasterizeLayer(target_ds, [1], source_layer, burn_values=[1])
    ##
    ###Find Distance
    target2_ds = gdal.GetDriverByName('GTiff').Create(raster2_fn, x_res, y_res, 1, gdal.GDT_CFloat32)
    target2_ds.SetGeoTransform((x_min, pixel_size, 0, y_max, 0, -pixel_size))

    ###Convert to Array
    myarray = np.array(target_ds.GetRasterBand(1).ReadAsArray())

    print myarray

    outputar = ndimage.morphology.distance_transform_edt(np.where(myarray==0,1, 0), sampling = 25)


    outBand = target2_ds.GetRasterBand(1)
    outBand.WriteArray(outputar)


    
source_ds = None
target_ds = None
target2_ds = None
##target3_ds = None
