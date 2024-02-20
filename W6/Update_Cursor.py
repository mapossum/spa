import arcpy

def magAdjust(mag):
    if mag < 1:
        return 1
    else:
        return mag * 2    


table = r'C:\Users\George\courses\spa\M6\Project\Week6_SPA\Week6_SPA.gdb\Tornados_Since_1970'

index=0
fields = arcpy.ListFields(table)
for field in fields:
    print(index, field.name)
    index = 1 + index
    
sr = arcpy.SpatialReference(4326)
rows = arcpy.da.UpdateCursor(table, '*', "", sr)


count = 0
for row in rows:
    mag = row[11]
    outval = magAdjust(mag)
    
    rows.updateRow(row) 
    count = count + 1
    if (count % 1000) == 0:
        print(row)

print("done")
