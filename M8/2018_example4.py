import arcpy

arcpy.env.workspace = r"C:\temp\spaLab\week8"
fc = r'Cityi10.shp'
fields = ['Name10', 'SHAPE@']

cursor = arcpy.da.SearchCursor(fc, fields)
for row in cursor:
    print('{0}, {1}'.format(row[0], row[1]))
