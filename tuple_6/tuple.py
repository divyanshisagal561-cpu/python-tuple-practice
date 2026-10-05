# 1. Create and Access
# Create a tuple containing 5 numbers. Print:

# The complete tuple
# First element
# Last element
# Third element

numbers_1 = (1, 2, 3, 4, 5)

print("Complete tuple", numbers_1)
print("First element:", numbers_1[0])
print("Last element:", numbers_1[-1])
print("Third element:", numbers_1[2])

# 2. Tuple Indexing
# Given:

numbers_2 = (10, 20, 30, 40, 50, 60)

# Print the elements using:

# Positive indexing
# Negative indexing

print("Using positive indexing:", numbers_2[0])
print("Using positive indexing:", numbers_2[1])
print("Using positive indexing:", numbers_2[2])
print("Using positive indexing:", numbers_2[3])
print("Using positive indexing:", numbers_2[4])
print("Using positive indexing:", numbers_2[5])

print("\nUsing negative indexing:", numbers_2[-1])
print("Using negative indexing:", numbers_2[-2])
print("Using negative indexing:", numbers_2[-3])
print("Using negative indexing:", numbers_2[-4])
print("Using negative indexing:", numbers_2[-5])
print("Using negative indexing:", numbers_2[-6])

# 3. Tuple Slicing
# Given:

numbers_3 = (10, 20, 30, 40, 50, 60, 70)

# Print:

# First 3 elements
# Last 3 elements
# Elements from index 2 to 5
# Tuple in reverse order

print("First 3 elements:", numbers_3[0:3])
print("Last 3 elements:", numbers_3[-3:])
print("Elements from index 2 to 5:", numbers_3[2:6])
print("Tuple in reverse order:", numbers_3[::-1])

# 4. Tuple Length
# Create a tuple containing 8 different values. Find its length using len().

numbers_4 = (10, 20, 30, 40, 50, 60, 70, 80)

length = len(numbers_4)
print("Length:", length)

# 5. Check Membership
# Given:

fruits = ("apple", "banana", "mango", "orange")

# Check whether "mango" and "grapes" exist in the tuple using in.

print("mango" in fruits)
print("grapes" in fruits)

# 6. Count Elements
# Given:

numbers_5 = (10, 20, 10, 30, 10, 40, 20)

# Find how many times 10 and 20 occur using count().

print(numbers_5.count(10))
print(numbers_5.count(20))

# 7. Find Index
# Given:

colors = ("red", "blue", "green", "yellow", "blue")

# Find the index of "green" and "blue" using index().

print(colors.index("green"))
print(colors.index("blue"))

# 8. Tuple Packing and Unpacking
# Create a tuple containing your:

# Name
# Age
# City

# Unpack the tuple into three separate variables and print them.

info = ("Divya", 18, "Delhi")

Name, Age, City = info

print(Name)
print(Age)
print(City)

# 9. Swap Variables Using Tuple
# Create two variables:

# a = 10
# b = 20

# Swap their values using tuple unpacking, without using a third variable.

a = 10
b = 20

a, b = b, a 

print("a:", a)
print("b:", b)

# 10. Nested Tuple
# Create:

# students = (
#     ("Rahul", 85),
#     ("Priya", 92),
#     ("Aman", 78)
# )

# Print:

# Priya's name
# Priya's marks
# Aman’s marks

students = (("Rahul", 85),
            ("Priya", 92),
            ("Aman", 78))

print(students[1][0])
print(students[1][1])
print(students[2][1])

# 11. Convert List to Tuple
# Create a list:

# list = [10, 20, 30, 40, 50]

# Convert it into a tuple and print both the original list and new tuple.

list_1 = [10, 20, 30, 40, 50]

new_tuple = tuple(list_1)

print("Original list:", list_1)
print("new tuple:", new_tuple)

# 12. Convert Tuple to List
# Given:

numbers_6 = (10, 20, 30, 40, 50)

# Convert it into a list, add 60, and convert it back into a tuple.

list_2 = list(numbers_6)

list_2.append(60)

new_tuple_2 = tuple(list_2)

print(new_tuple_2)

# 13. Tuple Concatenation and Repetition
# Given:

a = (1, 2, 3)
b = (4, 5, 6)

# Perform:

# Concatenation of a and b
# Repeat a three times

print("Concatenation:", a + b)

print("\nRepetition of a :", a * 3)
print("Repetition of b :", b * 3)

# 14. Find Maximum, Minimum and Sum
# Given:

numbers_7 = (25, 10, 45, 30, 15)

# Find:

# Maximum value
# Minimum value
# Sum of all values
# Average of the values

print("Maximum value:", max(numbers_7))
print("Minimum value:", min(numbers_7))

total = sum(numbers_7)
print("Sum of all value:", total)

avg = total / len(numbers_7)
print("Average of the value:", avg)

# 15. Tuple with Mixed Data Types ⭐
# Create a tuple containing:

# Your name
# Your age
# A list of 3 favorite subjects
# A dictionary containing city and country

# Then:

# Access your name
# Access the first subject
# Change the second subject in the list
# Access the city from the dictionary

info_2 = ("Divyanshi Sagal", 18, ["CS", "Eng", "Eco"], {"City":"New Delhi", "Country": "India"})

print("Name:", info_2[0])
print("First subject:", info_2[2][0])

info_2[2][1] = "Maths"
print("Changed tuple:", info_2)

print("City:",info_2[3]["City"])













