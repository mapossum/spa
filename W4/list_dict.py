john = {"name": "John", "age": 23, "profession": "Python Developer", "salary": 80000}
thomas = {"name": "Thomas", "age": 53, "profession": "Teacher", "salary": 15000}
barbara = {"name": "Barbara", "age": 30, "profession": "Doctor", "salary": 47000}

employees = [john, thomas, barbara]

print("Name", "Age")
for emp in employees:
    print("{}, {}".format(emp["name"],emp["age"]))
