# Name: Ly Nguyen
# ID: GCS210154
# Class: GCS1003A

#Exercise 1
number_list = [i for i in range(1, 21)]

# Slicing 1st half and 2nd half
first_half = number_list[:len(number_list)//2]
second_half = number_list[len(number_list)//2:]

# Remove n elements from 1st list and 2nd list
n = int(input("Enter the value of n: "))
sublist = number_list[n:len(number_list)-n]

# Put those 2 elements above to a new list (2n elements)
new_list = number_list[:n] + number_list[-n:]

print("First half:", first_half)
print("Second half:", second_half)
print(f"The list after remove 2n elements:", sublist)
print(f"New list with:", new_list)

#Exercise 2
#Create a 5 x 5 list of int numbers
lst = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]]

#Get 3 middle rows in different ways
middle_rows = lst[1:4]
print("3 middle rows: ")
for subarray in middle_rows:
    print(subarray)

#Get 2 last rows in different ways
last_rows = lst[3:5]
print("The last 2 rows: ", last_rows)

#4) Get max and min of the nth row entered by user
n = input("Enter row number (1-5): ")
row = lst[int(n) - 1]
max_val = max(row)
min_val = min(row)
print("Max value:", max_val)
print("Min value:", min_val)