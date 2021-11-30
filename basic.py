# Import random library to create random list of numbers
import random

# Generate 100 random numbers from 0 till 1000
b = [random.randrange(0, 1000, 1) for i in range(100)]
# Create empty list for sorted numbers
a = []
# Sort numbers from min to max
while b:
    minimum = b[0]  # arbitrary number in list
    for x in b:
        if x < minimum:
            minimum = x
    a.append(minimum)
    b.remove(minimum)
# Print the list with random numbers
print ("Sorted list:", a)

# Create empty list for even numbers
even = []
# Create empty list for odd numbers
odd = []

# Lookup in the random numbers list
for i in a:
    # Lookup for even numbers
    if i % 2 == 0:
        # Add evens to the list
        even.append(i)
    # Lookup for odd numbers
    elif i % 2 == 1:
        # Add odds to the list
        odd.append(i)

# Calculate odds average
odd_avg = sum(odd)/len(odd)
# Calculate evens average
even_avg = sum(even)/len(even)

#Print out lists and average values
print ("The list of evens:", even)
print ("The list of odds:", odd)
print ("Odd average is:", odd_avg)
print ("Even average is: ",  even_avg)

