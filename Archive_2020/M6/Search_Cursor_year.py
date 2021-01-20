import arcpy


for year in range(1970,2017):
    rows = arcpy.da.SearchCursor(r'C:\Users\George\courses\spa\M6\Project\Week6_SPA\Week6_SPA.gdb\Tornados_Since_1970', ("mag", "yr", "mo"), "yr = {}".format(year))

    count = 0
    magtotal = 0
    for row in rows:
        mag = row[0]
        #if (count % 1000) == 0:
        #    print(mag, count)
        if mag > 1:
            magtotal = mag + magtotal
            count = count + 1
    if count != 0:
        print("mean mag in {}:".format(year), magtotal / count, count)
    else:
        print("No Tornado Data in {}".format(year))
