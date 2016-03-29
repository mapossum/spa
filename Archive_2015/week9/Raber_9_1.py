import fiona
import shapely
import math
from shapely.geometry import shape, mapping

inputdataset = r"C:\temp\week8\Cityi10.shp"
outputDataset = r"C:\temp\week8\Cityi10_LM.shp"

c = fiona.open(inputdataset, 'r')

outdiver = c.driver
outschema = c.schema.copy()
outcrs = c.crs.copy()

#outschema['geometry'] = 'Polygon'
outschema['properties']['PARA'] = 'float'
outschema['properties']['ShapeIndex'] = 'float'
outschema['properties']['CIRCLE'] = 'float'
outschema['properties']['SCIRCLE'] = 'float'
print outschema

with fiona.open(outputDataset, 'w', driver=outdiver, crs=outcrs, schema=outschema) as w:

   for rec in c:
      geom = shape(rec["geometry"])
      prim = geom.length
      area = geom.area
      p_a = (prim/area)
      SI = p_a / ((math.sqrt(area) * 4)/area)
      
      
      rec['properties'].update(PARA=p_a)
      rec['properties'].update(ShapeIndex=SI)
      rec['properties'].update(CIRCLE=0)
      rec['properties'].update(SCIRCLE=0)
      
      w.write(rec)



