import fiona
import shapely
from shapely.geometry import shape, mapping
c = fiona.open(r'C:\spa\data\GPS_points.shp', 'r')

outdiver = c.driver
outschema = c.schema.copy()
outcrs = c.crs.copy()

#w = fiona.open(r'C:\spa\data\GPS_buffers.shp', 'w', driver=outdiver, crs=outcrs, schema=outschema)

#for rec in c:
#   w.write(rec)

#w.close()
#c.close()

outschema['geometry'] = 'Polygon'
outschema['properties']['newField'] = 'float'
print outschema

with fiona.open(r'C:\spa\data\GPS_buffers.shp', 'w', driver=outdiver, crs=outcrs, schema=outschema) as w:

   for rec in c:
      newgeo = shape(rec["geometry"]).buffer(100)
      newgeo2 = shape(rec["geometry"]).buffer(50)
      outg = newgeo.difference(newgeo2)
      rec["geometry"] = mapping(outg)
      rec['properties'].update(newField=10.1*8)
      w.write(rec)



