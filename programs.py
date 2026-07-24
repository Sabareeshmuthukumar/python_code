import sys
from datetime import datetime

# 1. Print Welcome
print("Welcome")

# 2. Print the given word
word = "Python"
print(word)

# 3. Print the given message
message = "Have a nice day"
print(message)

# 4. Print the given integer number
num = 25
print(num)

# 5. Print the given fractional number
frac = 3.14159
print(frac)

# 6. Print the given fractional number in 2-digit decimal format
print(f"{frac:.2f}")

# 7. Print the given integer number in hexadecimal format
print(hex(num))          # with 0x prefix
print(f"{num:x}")        # without prefix

# 8. Print the given integer number in octal format
print(oct(num))          # with 0o prefix
print(f"{num:o}")        # without prefix

# 9. Print the given hexadecimal number in integer format
hex_str = "0x19"
print(int(hex_str, 16))

# 10. Print the given octal number in integer format
oct_str = "0o31"
print(int(oct_str, 8))

# 11. Print the ASCII value of a character
ch = 'A'
print(ord(ch))

# 12. Print the character for the given ASCII value
ascii_val = 65
print(chr(ascii_val))

# 13. Print two numbers with a space between them
a, b = 10, 20
print(a, b)

# 14. Print two numbers with a tab space between them
print(f"{a}\t{b}")

# 15. Print two numbers in two lines
print(a)
print(b)

# 16. Print a character in single quotes
print(f"'{ch}'")

# 17. Print two words in double quotes
print('"Hello World"')

# 18. Print your date of birth in the format DD/MM/YYYY
dob = "15/08/2004"   # replace with your actual DOB
print(dob)

# 19. Print an integer with a plus sign (+) before it
positive_num = 42
print(f"{positive_num:+d}")

# 20. Print the size of char, int, float, and double
# Python has no fixed char/int/double types like C, so sizes are shown
# via sys.getsizeof() for Python's own object representation.
print("char (1 char str):", sys.getsizeof('a'), "bytes")
print("int:", sys.getsizeof(1), "bytes")
print("float:", sys.getsizeof(1.0), "bytes")
print("double (same as float in Python):", sys.getsizeof(1.0), "bytes")

# 21. Print your roll number and name
roll_no = 123
name = "John"
print(f"Roll No: {roll_no}, Name: {name}")

# 22. Print your marks in 5 subjects each on a new line
marks = [85, 90, 78, 92, 88]
for m in marks:
    print(m)

# 23. Print your blood group
blood_group = "O+"   # replace with your actual blood group
print(blood_group)

# 24. Print current time in the format HH:MM:SS
now = datetime.now()
print(now.strftime("%H:%M:%S"))

# 25. Print your address in multiple lines using \n
address = "123 Main Street\nNamakkal\nTamil Nadu\nIndia"
print(address)
