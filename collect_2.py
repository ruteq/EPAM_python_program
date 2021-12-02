import random


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
    for i in val1:
        d2[key] = random.choice(val1)

# Create result dictionary
# Set empty dict

d_res = {}
for (k,v), (k2,v2) in zip(d1.items(), d2.items()):

# If key value pair exists in the d1 and not in d2 it should be included into the result dict

    if k != k2:
        d_res[k] = v

# If key value pair exists in the d2 and not in d1 it should be included into the result dict

    if k2 != k:
        d_res[k2] = v2

# If the value in the d1 greater than value in the d2 for the same key this value should be included
# into the result dict. The key should be updated with '_1' suffix.

    if v > v2 and k == k2:
        d_res[k + '_1'] = v

# If the value in the d2 greater than value in the d1 for the same key this value should be included
# into the result dict. The key should be updated with '_2' suffix.

    if v < v2 and k == k2:
        d_res[k + '_2'] = v2


# Print out source dictionaries

print ("Dict_1:", d1)
print ("Dict_2:", d2)

# Print out result dictionary

print("Result dictionary:", d_res)
