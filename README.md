# Python Learning & Placement Preparation Repository

Welcome to the Python Learning repository! This repository contains a curated collection of Python programs, algorithms, data structure problems, placement preparation exercises, and Jupyter notebook practice problems written during placement training and logic building sessions.

---

## 📋 Table of Contents

- [Repository Overview](#repository-overview)
- [File Structure](#file-structure)
- [1. Logical & Algorithmic Interview Problems (`logics.py`)](#1-logical--algorithmic-interview-problems-logicspy)
- [2. Placement & Basic Fundamentals (`programs.py`)](#2-placement--basic-fundamentals-programspy)
- [3. Algorithm Practice Scripts](#3-algorithm-practice-scripts)
  - [Trapping Rain Water (`practice.py`)](#trapping-rain-water-practicepy)
  - [Matrix Initialization Snippet (`practice1.py`)](#matrix-initialization-snippet-practice1py)
- [4. Notebook Practice Exercises (`practice.ipynb`)](#4-notebook-practice-exercises-practiceipynb)
- [How to Run](#how-to-run)

---

## 🔍 Repository Overview

This project serves as a comprehensive reference guide for:
- Core Python syntax, data types, and formatting operations.
- Classic array manipulation, string algorithms, two-pointer techniques, and bitwise tricks.
- Mathematical operations, number theory, and pattern generation.
- Interview-ready solutions verified with test suites.

---

## 📁 File Structure

| File | Description |
| :--- | :--- |
| [logics.py](file:///c:/Users/sabar/Downloads/python/logics.py) | Top 12 LeetCode / Interview algorithmic solutions with type hints and test assertions. |
| [programs.py](file:///c:/Users/sabar/Downloads/python/programs.py) | 25 foundational Python programs covering I/O, base conversions, data types, and formatting. |
| [practice.py](file:///c:/Users/sabar/Downloads/python/practice.py) | Dynamic programming solution for the Trapping Rain Water problem. |
| [practice1.py](file:///c:/Users/sabar/Downloads/python/practice1.py) | Nested list and matrix initialization practice. |
| [practice.ipynb](file:///c:/Users/sabar/Downloads/python/practice.ipynb) | Interactive notebook with 20+ logic-building exercises (matrices, sorting, number theory, patterns). |

---

## 1. Logical & Algorithmic Interview Problems (`logics.py`)

File: [logics.py](file:///c:/Users/sabar/Downloads/python/logics.py)

Contains 12 essential interview problems complete with time/space complexity analysis and inline assertions.

```python
from typing import List, Dict, Tuple, Optional

# ==============================================================================
# SECTION 1: ARRAYS & TWO POINTERS
# ==============================================================================

# 1. Two Sum (Time: O(n), Space: O(n))
def two_sum(nums: List[int], target: int) -> List[int]:
    seen: Dict[int, int] = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

# 2. Kadane's Algorithm - Maximum Subarray Sum (Time: O(n), Space: O(1))
def max_sub_array(nums: List[int]) -> int:
    max_so_far = nums[0]
    current_max = nums[0]
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far

# 3. Container With Most Water (Time: O(n), Space: O(1))
def container_with_most_water(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        current_water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, current_water)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

# 4. Move Zeroes In-Place (Time: O(n), Space: O(1))
def move_zeroes(nums: List[int]) -> None:
    write_idx = 0
    for read_idx in range(len(nums)):
        if nums[read_idx] != 0:
            nums[write_idx], nums[read_idx] = nums[read_idx], nums[write_idx]
            write_idx += 1

# ==============================================================================
# SECTION 2: STRINGS & SLIDING WINDOW
# ==============================================================================

# 5. Valid Palindrome (Time: O(n), Space: O(1))
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

# 6. Longest Substring Without Repeating Characters (Time: O(n), Space: O(min(n, m)))
def length_of_longest_substring(s: str) -> int:
    char_map: Dict[str, int] = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

# 7. Group Anagrams (Time: O(n * k log k), Space: O(n * k))
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map: Dict[str, List[str]] = {}
    for word in strs:
        sorted_key = "".join(sorted(word))
        if sorted_key not in anagram_map:
            anagram_map[sorted_key] = []
        anagram_map[sorted_key].append(word)
    return list(anagram_map.values())

# ==============================================================================
# SECTION 3: MATH, BITWISE & LOGIC PUZZLES
# ==============================================================================

# 8. Single Number via Bitwise XOR (Time: O(n), Space: O(1))
def single_number(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res

# 9. Missing Number using Gauss Summation (Time: O(n), Space: O(1))
def missing_number(nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)

# 10. Fibonacci Number (Iterative, Time: O(n), Space: O(1))
def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# ==============================================================================
# SECTION 4: STACKS & DYNAMIC PROGRAMMING
# ==============================================================================

# 11. Valid Parentheses Matching (Time: O(n), Space: O(n))
def is_valid_parentheses(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map:
            top = stack.pop() if stack else '#'
            if bracket_map[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

# 12. Product of Array Except Self (Time: O(n), Space: O(1) extra space)
def product_except_self(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = [1] * n
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    return result
```

---

## 2. Placement & Basic Fundamentals (`programs.py`)

File: [programs.py](file:///c:/Users/sabar/Downloads/python/programs.py)

A set of 25 basic programs demonstrating essential Python features and I/O techniques.

```python
import sys
from datetime import datetime

# 1. Print Welcome
print("Welcome")

# 2. Print given word
word = "Python"
print(word)

# 3. Print given message
message = "Have a nice day"
print(message)

# 4. Print given integer
num = 25
print(num)

# 5. Print given fractional number
frac = 3.14159
print(frac)

# 6. Format fractional number to 2 decimal places
print(f"{frac:.2f}")

# 7. Print integer in hexadecimal format
print(hex(num))          # with 0x prefix
print(f"{num:x}")        # without prefix

# 8. Print integer in octal format
print(oct(num))          # with 0o prefix
print(f"{num:o}")        # without prefix

# 9. Convert hexadecimal string to integer
hex_str = "0x19"
print(int(hex_str, 16))

# 10. Convert octal string to integer
oct_str = "0o31"
print(int(oct_str, 8))

# 11. ASCII value of a character
ch = 'A'
print(ord(ch))

# 12. Character from ASCII value
ascii_val = 65
print(chr(ascii_val))

# 13. Print two numbers separated by space
a, b = 10, 20
print(a, b)

# 14. Print two numbers separated by tab
print(f"{a}\t{b}")

# 15. Print two numbers in separate lines
print(a)
print(b)

# 16. Print character in single quotes
print(f"'{ch}'")

# 17. Print text in double quotes
print('"Hello World"')

# 18. Print Date of Birth
dob = "15/08/2004"
print(dob)

# 19. Print integer with plus sign prefix
positive_num = 42
print(f"{positive_num:+d}")

# 20. Check object sizes in memory (bytes)
print("char (1 char str):", sys.getsizeof('a'), "bytes")
print("int:", sys.getsizeof(1), "bytes")
print("float:", sys.getsizeof(1.0), "bytes")
print("double:", sys.getsizeof(1.0), "bytes")

# 21. Print roll number and name
roll_no = 123
name = "John"
print(f"Roll No: {roll_no}, Name: {name}")

# 22. Print subject marks
marks = [85, 90, 78, 92, 88]
for m in marks:
    print(m)

# 23. Print blood group
blood_group = "O+"
print(blood_group)

# 24. Print current time (HH:MM:SS)
now = datetime.now()
print(now.strftime("%H:%M:%S"))

# 25. Print multi-line address
address = "123 Main Street\nNamakkal\nTamil Nadu\nIndia"
print(address)
```

---

## 3. Algorithm Practice Scripts

### Trapping Rain Water (`practice.py`)

File: [practice.py](file:///c:/Users/sabar/Downloads/python/practice.py)

Calculates the total trapped water between bars of given heights using precomputed left and right prefix maximum arrays.

```python
# Trapping Rain Water Solution
height = [0, 1, 0, 1]
n = len(height)

if n == 0:
    print(0)
else:
    left_max = [0] * n
    left_max[0] = height[0]

    right_max = [0] * n
    right_max[n - 1] = height[n - 1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    print(water)
```

### Matrix Initialization Snippet (`practice1.py`)

File: [practice1.py](file:///c:/Users/sabar/Downloads/python/practice1.py)

```python
i = 2
mat = [[] * i]
print(mat)
```

---

## 4. Notebook Practice Exercises (`practice.ipynb`)

File: [practice.ipynb](file:///c:/Users/sabar/Downloads/python/practice.ipynb)

A collection of interactive practice cells covering core logic building tasks:

### 1. Matrix Operations (Addition, Row-wise & Column-wise Sum)
```python
# 2D Matrix Addition
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of cols: "))
matrix1, matrix2, result = [], [], []

for i in range(rows):
    row = [int(input("enter value: ")) for _ in range(cols)]
    matrix1.append(row)

for i in range(rows):
    row = [int(input("enter value: ")) for _ in range(cols)]
    matrix2.append(row)

for i in range(rows):
    result.append([matrix1[i][j] + matrix2[i][j] for j in range(cols)])

print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Sum Result:", result)
```

### 2. Sorting & Search Logic
```python
# Bubble Sort Implementation
def bubble_sort(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

# Move Zeroes to End of List
l = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]
zeros = [x for x in l if x == 0]
non_zeros = [x for x in l if x != 0]
result = non_zeros + zeros
print(result)
```

### 3. Number Theory & Logic Checks
```python
# Check Armstrong Number
n = int(input("Enter number: "))
org = n
total_sum = 0
while n > 0:
    digit = n % 10
    total_sum += digit ** 3
    n //= 10

if total_sum == org:
    print("Armstrong")
else:
    print("Not Armstrong")

# Decimal to Binary Conversion
decimal_num = int(input("Enter decimal: "))
if decimal_num == 0:
    binary_str = "0"
else:
    binary_str = ""
    while decimal_num > 0:
        binary_str = str(decimal_num % 2) + binary_str
        decimal_num //= 2
print("Binary:", binary_str)
```

### 4. Pattern Printing
```python
# Right Triangle Star Pattern
for i in range(1, 6):
    print("* " * i)

# Inverted Triangle Star Pattern
for i in range(5, 0, -1):
    print("* " * i)
```

---

## 🚀 How to Run

### Running Python Scripts
Run any of the Python files directly using the `python` interpreter:

```bash
python logics.py
python programs.py
python practice.py
```

### Running the Verification Test Suite
`logics.py` comes with a built-in test suite. Execute it to verify all 12 algorithms:

```bash
python logics.py
```

Expected output:
```text
============================================================
 Running Verification Tests for Python Interview Problems 
============================================================
[OK] 1. Two Sum: Passed
[OK] 2. Kadane's Algorithm: Passed
[OK] 3. Container With Most Water: Passed
[OK] 4. Move Zeroes: Passed
[OK] 5. Valid Palindrome: Passed
[OK] 6. Longest Substring: Passed
[OK] 7. Group Anagrams: Passed
[OK] 8. Single Number: Passed
[OK] 9. Missing Number: Passed
[OK] 10. Fibonacci: Passed
[OK] 11. Valid Parentheses: Passed
[OK] 12. Product Except Self: Passed

All 12 Interview Logical Problems Executed and Verified Successfully!
```

---

*Happy Coding! 🚀*
