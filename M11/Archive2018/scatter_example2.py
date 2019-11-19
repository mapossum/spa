"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt

x = [1.0,2.0,3.0,4.1,5.2]
y = [2.0,3.0,5.3,7.2,9.1]
area = 10 

m,b = np.polyfit(x, y, 1)
print m, b

results = {}
results['polynomial'] = [m,b]
correlation = np.corrcoef(x, y)[0,1]

print correlation 

plt.scatter(x, y, s=area, alpha=0.5)
#plt.plot(x, m*x + b, '-')
plt.show()
