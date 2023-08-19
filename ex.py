# Finding The largest Value in Python!

numbers = [12, 30, 49, 154, 65, 98]

largest = None

for value in numbers :
    if largest is None : 
        largest = value
    elif value > largest :
        largest = value
print(largest)            