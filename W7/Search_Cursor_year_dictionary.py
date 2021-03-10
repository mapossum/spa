import arcpy



rows = arcpy.da.SearchCursor(r'C:\Users\George\courses\spa\M6\Project\Week6_SPA\Week6_SPA.gdb\Tornados_Since_1970', ("mag", "yr", "mo"))

yearsDict = {}

for year in range(1970,2018):
    yearsDict[year] = {"sum" : 0 , "count": 0}

count = 0
magtotal = 0
for row in rows:
    mag = row[0]
    yr = row[1]
    #if (count % 1000) == 0:
    #    print(mag, count)
    if mag > 1:
        yearsDict[yr]["sum"] = mag + yearsDict[yr]["sum"]
        yearsDict[yr]["count"] = yearsDict[yr]["count"] + 1

for year in range(1970,2018):        
    if yearsDict[year]["count"] != 0:
        print("mean mag in {}:".format(year), yearsDict[year]["sum"] / yearsDict[year]["count"], yearsDict[year]["count"])
    else:
        print("No Tornado Data in {}".format(year))
