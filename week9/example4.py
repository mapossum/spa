import fiona
import shapely
import math
import SEC
from shapely.geometry import shape, mapping

outputDataset = r"C:\temp\week8\Cityi10.shp"


with fiona.open(outputDataset, 'r') as c:
    print c.schema
    for rec in c:
        coordlist = []
        newgeo = mapping(shape(rec["geometry"]).buffer(1))
        rings = newgeo["coordinates"]
        print type(rings), len(rings), rec["properties"]["NAME10"]
        for ring in rings:
            for coord in ring:
                coordlist.append(coord)

        try:
            minCircle = SEC.make_circle(coordlist)
        except:
            print "didn't work"
