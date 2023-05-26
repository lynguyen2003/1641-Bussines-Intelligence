# Name: Ly Nguyen
# ID:GCS210154
# Class: GCS1003A

# ===========================================
# Exercise 1:

# Modified text function
def modified_text(text, order, word_replace):
    words = text.split()
    words[order-1] = word_replace
    return " ".join(words) 

# Count original text function
def count_original_text(text):
    words = text.split()
    return len(words)

# Count modified text function
def count_modified_text(new_text):
    words = new_text.split()
    return len(words)

# Data input
text = input("Text: ")
order = int(input("Order: "))
word_replace = input("Word replace: ")

# Text after modified 
new_text = modified_text(text, order, word_replace)

# Print result to screen 
print(new_text)
print("Length of original text is: ", count_original_text(text))
print("Modified text is: ", word_replace)
print("Length of modified text is: ", count_modified_text(new_text))

# ===========================================
# Exercise 2:

# Variables
# name = "Ly Nguyen"
# age = "18"
# student_year = 2023-2021

# Print to screen
# print("My name is ", name ,"and I am ", age ,"years old.")
# print("I am ", student_year ," year student at Greenwich University")