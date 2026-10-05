# 🐍 Python Tuple Practice

A beginner-friendly Python practice project covering the **fundamentals of Tuples** through 15 practical exercises.

This project demonstrates how to create, access, modify, manipulate, and work with tuples in Python, along with tuple-related operations such as indexing, slicing, packing, unpacking, concatenation, repetition, and type conversion.

---

## 📌 Project Overview

Tuples are one of Python's built-in collection data types. They are **ordered and immutable**, making them useful when data should remain unchanged.

This project was created to strengthen practical understanding of Python tuples through small, focused coding exercises.

---

## 🎯 Learning Objectives

By completing this project, you will practice:

* Creating and accessing tuples
* Positive and negative indexing
* Tuple slicing
* Finding tuple length
* Membership operators
* Counting elements
* Finding element indexes
* Tuple packing and unpacking
* Swapping variables using tuple unpacking
* Working with nested tuples
* Converting lists to tuples
* Converting tuples to lists
* Tuple concatenation
* Tuple repetition
* Using `max()`, `min()`, `sum()`, and `len()`
* Working with mixed data types inside tuples
* Modifying mutable objects stored inside tuples

---

## 📚 Topics Covered

### 1. Create and Access Tuples

Creates a tuple containing five numbers and accesses specific elements.

```python
numbers = (1, 2, 3, 4, 5)

print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2])
```

### 2. Tuple Indexing

Demonstrates both:

* Positive indexing
* Negative indexing

### 3. Tuple Slicing

Examples include:

* First 3 elements
* Last 3 elements
* Elements from a specific index range
* Reversing a tuple

```python
numbers[::-1]
```

### 4. Tuple Length

Uses the `len()` function to determine the number of elements.

### 5. Membership Checking

Uses the `in` operator to check whether an element exists in a tuple.

```python
"mango" in fruits
```

### 6. Counting Elements

Uses the `count()` method to determine how many times a value occurs.

### 7. Finding an Index

Uses the `index()` method to find the position of an element.

### 8. Tuple Packing & Unpacking

Demonstrates how multiple values can be packed into a tuple and unpacked into separate variables.

```python
info = ("Divya", 18, "Delhi")

Name, Age, City = info
```

### 9. Swapping Variables

Uses tuple unpacking to swap two variables without a third variable.

```python
a, b = b, a
```

### 10. Nested Tuples

Demonstrates accessing elements from tuples contained inside another tuple.

```python
students[1][0]
students[1][1]
```

### 11. List → Tuple

Converts a Python list into a tuple using `tuple()`.

### 12. Tuple → List → Tuple

Converts a tuple into a list, modifies the list, and converts it back into a tuple.

### 13. Tuple Concatenation & Repetition

Demonstrates:

```python
a + b
a * 3
```

### 14. Maximum, Minimum, Sum & Average

Uses Python built-in functions to perform calculations on tuple values.

```python
max(numbers)
min(numbers)
sum(numbers)
len(numbers)
```

The average is calculated using:

```python
average = total / len(numbers)
```

### 15. Mixed Data Types

Demonstrates storing different data types inside a tuple, including:

* String
* Integer
* List
* Dictionary

It also demonstrates an important concept: although tuples are immutable, **mutable objects such as lists inside a tuple can still be modified**.

---

## 🗂️ Project Structure

```text
Python-Tuple-Practice/
│
├── tuple.py
└── screenshots.png
└── README.md
```

---

## 🛠️ Technologies Used

| Technology        | Purpose                             |
| ----------------- | ----------------------------------- |
| 🐍 Python         | Programming language               |
| 💻 VS Code       | Code development                    |
| 🔧 Git & GitHub   | Version control and project hosting |

---

## 💡 Key Concepts Learned

Through this project, I practiced how Python tuples work and how they differ from mutable collections such as lists.

Some important concepts demonstrated include:

```text
Tuple Creation
      ↓
Indexing
      ↓
Slicing
      ↓
Tuple Methods
      ↓
Packing & Unpacking
      ↓
Nested Tuples
      ↓
Type Conversion
      ↓
Tuple Operations
      ↓
Mixed Data Types
```

---


## 👩‍💻 Author

**Divyanshi Sagal**

BCA Student 

Interested in:

* 🐍 Python
* 📊 Data Analysis
* 🗄️ SQL
* 📈 Data Analytics

---

## ⭐ Acknowledgement

This project was created as part of my Python learning and practice journey, with a focus on building strong fundamentals through hands-on coding.

If you find this project useful, consider giving the repository a ⭐.
