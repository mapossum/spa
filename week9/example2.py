import fiona

c = fiona.open(r'C:\spa\data\GPS_points.shp', 'r')


outdiver = c.driver
outschema = c.schema.copy()
outcrs = c.crs.copy()

w = fiona.open(r'C:\spa\data\GPS_buffers.shp', 'w', driver=outdiver, crs=outcrs, schema=outschema)

for rec in c:
   w.write(rec)


w.close()
c.close()
