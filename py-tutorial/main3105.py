# Name: Ly Nguyen
# ID: GCS210154
# Class: GCS1003A

# Exercise 6
import numpy as np

# Use linspace when you want to generate a sequence of evenly spaced numbers within a specified range.
array_a = np.linspace(0, 20, 10, dtype=int)
print(array_a)

# Use arange when you want to generate a sequence of numbers with a specified step size.
array_b = np.arange(0, 20, 2, dtype=int)
print(array_b)

# Exercise 7
names = ["Ly", "", "Nguyen", "Thanh", "", "Sen"]
ages = [8, 20, -1, 35, 100, 45]

# Change empty names to "John Doe"
for i in range(len(names)):
    if names[i] == "":
        names[i] = "John Doe"

# Correct invalid ages
for i in range(len(ages)):
    if ages[i] < 0:
        ages[i] = 0
    elif ages[i] > 150:
        ages[i] = 150

# Find max age and min age
max_age = max(ages)
min_age = min(ages)

print("Names:", names)
print("Ages:", ages)
print("Max age:", max_age)
print("Min age:", min_age)

# Find longest and shortest names
longest_name = max(names, key=len)
shortest_name = min(names, key=len)

# Find length of longest and shortest names
longest_length = len(longest_name)
shortest_length = len(shortest_name)

print("Longest name:", longest_name)
print("Shortest name:", shortest_name)
print("Length of longest name:", longest_length)
print("Length of shortest name:", shortest_length)

# Exercise 8:
import numpy as np
# Create an 8x8 array with ones on all the edges and zeros everywhere else.
a = np.zeros((8, 8))
a[0, :] = 1
a[-1, :] = 1
a[:, 0] = 1
a[:, -1] = 1

print("a) Array with ones on edges:", a)