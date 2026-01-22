"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt
import arcpy
area = 10

# Create two Random arrays
#N = 50
#x = np.random.rand(N)
#y = np.random.rand(N)

#Read in a feature class and choose two of the columns (fields)
#use Correlation and Regression to examine how they are related

fc = r'C:\temp\FinalData.gdb\Question2Features'
fields = ['AvgDLSpF', 'Latitude']

xlist =  [] #Store all the Latitude Data as a list
ylist =  [] #Store all the average day of Last Spring Frost Data a list
for row in arcpy.da.SearchCursor(fc, fields):
    ylist.append(row[0]) #value for this row of AvgDLSpF
    xlist.append(row[1]) #value for this row of Latitude

#Convert the lists to numpy arrays
x=np.asarray(xlist)
y=np.asarray(ylist)

m,b = np.polyfit(x, y, 1)
print(m, b)

results = {}
results['polynomial'] = [m,b]
correlation = np.corrcoef(x, y)[0,1]

print(correlation)

plt.scatter(x, y, s=area, alpha=0.5)
plt.plot(x, m*x + b, '-')

#You can save or show it (one or the other not both).
#plt.show()
plt.savefig(r'c:\temp\NameofPlot.png')
