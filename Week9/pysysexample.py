import sys, arcpy
import numpy as np

allargs = sys.argv[1:]

allnumbers = True
for args in allargs:
    if not args.isnumeric():
        allnumbers = False

if allnumbers:
    arcpy.AddMessage(np.asarray(allargs).astype(float).sum())

else:
    arcpy.AddError("All arguments are not numeric " + str(allargs))

