import numpy as np

x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])


print(x[1]) #What will that give?

print(x["age"]) #What will this give

print(x[1]["age"]) #What will this give

x["age"] = x["age"] + 2

