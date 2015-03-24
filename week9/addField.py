from osgeo import ogr

def addFloatField(path, fieldName)
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(path, 1) #1 is read/write

    #define floating point field named DistFld and 16-character string field named Name:
    fldDef = ogr.FieldDefn(fieldName, ogr.OFTReal)

    layer = dataSource.GetLayer()
    layer.CreateField(fldDef)
    del layer
    del dataSource
    del driver


def addStringField(path, fieldName, width)
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(path, 1) #1 is read/write

    fldDef2 = ogr.FieldDefn(fieldName, ogr.OFTString)
    fldDef2.SetWidth(width) 

    #get layer and add the 2 fields:
    layer = dataSource.GetLayer()
    layer.CreateField(fldDef2)
    del layer
    del dataSource
    del driver

def addIntegerField(path, fieldName)
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(path, 1) #1 is read/write

    #define floating point field named DistFld and 16-character string field named Name:
    fldDef = ogr.FieldDefn(fieldName, ogr.OFTInteger)

    layer = dataSource.GetLayer()
    layer.CreateField(fldDef)
    del layer
    del dataSource
    del driver
    
