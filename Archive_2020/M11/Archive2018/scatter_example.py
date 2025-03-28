"""
Simple demo of a scatter plot.
"""
import numpy as np
import matplotlib.pyplot as plt


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = 10 

m,b = np.polyfit(x, y, 1)
print(m, b)

results = {}
results['polynomial'] = [m,b]
correlation = np.corrcoef(x, y)[0,1]

print(correlation)

plt.scatter(x, y, s=area, alpha=0.5)
plt.plot(x, m*x + b, '-')

#You can save or show it (one or the other not both).
plt.show()
#plt.savefig(r'c:\temp\NameofPlot.png')
