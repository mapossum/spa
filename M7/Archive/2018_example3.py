import arcpy

arcpy.env.workspace = r"C:\temp\spaLab\week8"
fc = r'GPS_points.shp'
fields = ['Time', 'Animal', 'SHAPE@']

cursor = arcpy.da.SearchCursor(fc, fields)
for row in cursor:
    print('{0}, {1}, {2}'.format(row[0], row[1], row[2].centroid))
