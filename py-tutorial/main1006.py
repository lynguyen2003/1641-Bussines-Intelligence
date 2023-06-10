# Name: Ly Nguyen
# ID: GCS210154
# Class: GCS1003A

#Exercise 6:
# 6. Create 2 arrays of same size for names and ages, including some empty names, invalid ages (less than 0, over 150)
# a) For any empty name, change it to “John Doe”
# b) For any invalid age, correct it to 0 or 150 correspondingly
# c) Find max age, min age
# d) *Find longest name, shortest name
# e) **Find length of longest name, length of shortest name (without knowing which it is)

import numpy as np
import pandas as pd
import matplotlib as plt
from itertools import chain 


names = np.array(["Ly", "", "Nguyennnnn", "Thanh", "Sen_1", "Sen_2", "Sen_3", "Sen_4", "Sen_5"])
ages = np.array([14, 25, 63, 722, 25, 64, 46, -35, 0])

#a)For any empty name, change it to “John Doe”
names[names==""] = "John Doe"
print("a) Change empty string: ", names)

#b)For any invalid age, correct it to 0 or 150 correspondingly
ages1 = ages
ages[ages < 0] = 0
ages[ages > 150] = 150
print("b) \nMethod 1: ", ages)

ages1 = np.clip(ages1, 0, 150)
print("\nMethod 2: ", ages1)

#c) Find max age, min age
max_age = np.max(ages)
print("c) Max age: ", max_age)

#d) Find longest name, shortest name

# Find the length of each name
name_lengths = np.char.str_len(names)

# Find the index of the longest name
longest_name_index = np.argmax(name_lengths)

# Find the index of the shortest name
shortest_name_index = np.argmin(name_lengths)

# Retrieve the actual longest and shortest names
longest_name = names[longest_name_index]
shortest_name = names[shortest_name_index]

# Print the results
print("Longest name:", longest_name)
print("Shortest name:", shortest_name)

# e) **Find length of longest name, length of shortest name (without knowing which it is)
        