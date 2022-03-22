from sys import argv

# Bubble sort improved

list = [1, -7, 2, 5, 3 , 9]

lenght = len(list) # find lenght list
    
for i in range(0, lenght - 1):
    for j in range(0, lenght - 1 - i):
        if list[j] < list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)

# Bubble sort descending

list = [1, -7, 2, 5, 3 , 9]

for i in range(0, lenght - 1):
    for j in range(0, lenght - 1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)

# output
# [9, 5, 3, 2, 1, -7]
# [-7, 1, 2, 3, 5, 9]