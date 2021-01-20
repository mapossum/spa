"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
import arcpy

bathy = arcpy.RasterToNumPyArray(r"C:\temp\GOM.gdb\bathy")
SST = arcpy.RasterToNumPyArray(r"C:\temp\GOM.gdb\MeanAnnualSalinity")

bathy = np.reshape(bathy, bathy.size)
SST = np.reshape(SST, SST.size)

b = np.where(bathy != 0)
bathy = bathy[b]
SST = SST[b]

c = np.where(bathy > -6000)
bathy = bathy[c]
SST = SST[c]

d = np.where(SST > 0)
bathy = bathy[d]
SST = SST[d]

print SST

x = bathy
y = SST
area = 10

m,b = np.polyfit(x, y, 1)
print m, b

results = {}
results['polynomial'] = [m,b]
correlation = np.corrcoef(x, y)[0,1]

print correlation 

plt.scatter(x, y, s=area, alpha=0.5)
plt.plot(x, m*x + b, '-')
plt.show()
