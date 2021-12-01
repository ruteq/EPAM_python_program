import random
from collections import defaultdict

# Generate random values for dictionary 1
val = [random.randrange(0, 40, 1) for i in range(7)]
# Generate random values for dictionary 2
val1 = [random.randrange(0, 50, 1) for i in range(7)]
# Keys set for dictionaries
keys1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
keys2 = ['a', 'b', 'c', 'd', 'e', 'n', 'g']
# Create dictionary 1
d1 = {}
for key in keys1:
    for i in val:
        d1[key] = random.choice(val)

# Create dictionary 2
d2 = {}
for key in keys2:
    for i in val:
        d2[key] = random.choice(val1)

d_res = {}
#d_res = defaultdict(int)
for key,value in d2.items():
    for key, value in d1.items():
        if d2.values() >

# Print out values for dict1
print ("Values:", val)
# Print out values for dict2
print ("Values_1:", val1)
# Print out keys
#print("Keys:", keys)
# Print out dictionaries
print ("Dict_1:", d1)
print ("Dict_2:", d2)
# Print out result dictionary
print("Result dictionary:", d_res)
