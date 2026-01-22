import arcpy
rows = arcpy.da.SearchCursor(r'C:\Users\George\courses\spa\M6\Project\Week6_SPA\Week6_SPA.gdb\Tornados_Since_1970', ("mag", "yr", "mo"))

count = 0
magtotal = 0
for row in rows:
    mag = row[0]
    count = count + 1
    #if (count % 1000) == 0:
    #    print(mag, count)
    if mag > 1:
        magtotal = mag + magtotal

        

print("mean mag:", magtotal / count)
