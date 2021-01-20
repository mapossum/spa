import arcpy

arcpy.env.overwriteOutput = True

fc = r"C:\temp\M7\Cityi10.shp"

desc = arcpy.Describe(fc)
fieldList = desc.fields

fields = []
for field in fieldList:
    if field.type == "Geometry":
        fields.append("SHAPE@")
    elif field.type != "OID":
        fields.append(field.name)

cursor1 = arcpy.da.SearchCursor(fc, fields, "NAME10 LIKE '%'")

out_path = r"C:\temp\M7"
out_name = "Cityi10_Convex.shp"
arcpy.CreateFeatureclass_management(out_path, out_name, "Polygon", fc, "", "", fc)
arcpy.AddField_management(r"{}\{}".format(out_path,out_name), "SHAPE_AREA", "DOUBLE")

fields.append("SHAPE_AREA")
cursor2 = arcpy.da.InsertCursor(r"{}\{}".format(out_path,out_name), fields)

for row in cursor1:
    #shape = row[0]
    #newgeometry = shape.convexHull()
    #newgeometryDiff = newgeometry.buffer(200).difference(shape)
    shape = row[0].convexHull().difference(row[0])
    outrow = []
    for val in row:
        outrow.append(val)
    outrow[0] = shape
    print(outrow)
    outrow.append(shape.getArea() / row[0].getArea())
    cursor2.insertRow(outrow)

del cursor1, cursor2
