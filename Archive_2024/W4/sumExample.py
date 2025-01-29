a_list = [1, 2, 3, 0, 5, 10, 11]

#Sum is a REDUCE function

builtinSum = sum(a_list)

print(builtinSum)

total = 0
for num in a_list:
    total = num + total

print(total)


#Conversion is a MAP function

index = 0
while index < len(a_list):
    a_list[index] = a_list[index] * 3.028
    index = index + 1

print(a_list)

#equiv using range

for index in range(len(a_list)):
    a_list[index] = a_list[index] / 3.028

print(a_list)

#Filter Function example

b_list = []
for num in a_list:
    if num > 8:
        b_list.append(num)

print(b_list)

