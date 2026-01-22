import fiona

c = fiona.open(r'C:\spa\data\GPS_points.shp', 'r')

print c.crs
print c.schema

for rec in c:
    print rec
