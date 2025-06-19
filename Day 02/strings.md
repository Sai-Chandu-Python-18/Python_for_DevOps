# Strings

**1. String Data Type in Python:**

- In Python, a string is a sequence of characters, enclosed within single (' '), double (" "), or triple (''' ''' or """ """) quotes.
- Strings are immutable, meaning you cannot change the characters within a string directly. Instead, you create new strings.
- You can access individual characters in a string using indexing, e.g., `my_string[0]` will give you the first character.
- Strings support various built-in methods, such as `len()`, `upper()`, `lower()`, `strip()`, `replace()`, and more, for manipulation.

**2. String Manipulation and Formatting:**

- Concatenation: You can combine strings using the `+` operator.
- Substrings: Use slicing to extract portions of a string, e.g., `my_string[2:5]` will extract characters from the 2nd to the 4th position.
- String interpolation: Python supports various ways to format strings, including f-strings (f"...{variable}..."), %-formatting ("%s %d" % ("string", 42)), and `str.format()`.
- Escape sequences: Special characters like newline (\n), tab (\t), and others are represented using escape sequences.
- String methods: Python provides many built-in methods for string manipulation, such as `split()`, `join()`, and `startswith()`.

**There are Different types of Inbuilt methods in Strings:**
Python String Inbuilt Methods (Cheat Sheet)
Python strings come with powerful built-in methods for manipulation, searching, formatting, and validation. Here’s a structured guide:

**1. Case Conversion**

Method	Description	Example
str.lower()	Convert to lowercase	"HELLO".lower() → "hello"
str.upper()	Convert to uppercase	"hello".upper() → "HELLO"
str.title()	Capitalize each word	"hello world".title() → "Hello World"
str.capitalize()	Capitalize first character	"python".capitalize() → "Python"
str.swapcase()	Swap uppercase/lowercase	"PyThOn".swapcase() → "pYtHoN"

**2. Searching & Validation**
Method	Description	Example
str.startswith()	Check if string starts with a substring	"hello".startswith("he") → True
str.endswith()	Check if string ends with a substring	"world".endswith("ld") → True
str.find()	Return index of first occurrence (or -1)	"apple".find("p") → 1
str.index()	Like find(), but raises ValueError	"apple".index("z") → Error
str.count()	Count occurrences of substring	"banana".count("a") → 3
str.isalpha()	Check if all characters are alphabetic	"abc".isalpha() → True
str.isdigit()	Check if all characters are digits	"123".isdigit() → True
str.isalnum()	Check if alphanumeric (letters + numbers)	"abc123".isalnum() → True

**3. String Manipulation**
Method	Description	Example
str.strip()	Remove leading/trailing whitespace	" hi ".strip() → "hi"
str.lstrip()	Remove leading whitespace	" hi".lstrip() → "hi"
str.rstrip()	Remove trailing whitespace	"hi ".rstrip() → "hi"
str.replace()	Replace occurrences of a substring	"hello".replace("l", "x") → "hexxo"
str.split()	Split into a list by delimiter (default: space)	"a,b,c".split(",") → ["a", "b", "c"]
str.join()	Join iterable into a string	",".join(["a", "b"]) → "a,b"
str.zfill()	Pad with zeros (for numbers)	"42".zfill(5) → "00042"


**4. Formatting & Alignment**
Method	Description	Example
str.format()	Format placeholders ({})	"{}".format(42) → "42"
f-strings	Modern formatting (Python 3.6+)	f"Value: {42}" → "Value: 42"
str.ljust()	Left-align with padding	"hi".ljust(5) → "hi "
str.rjust()	Right-align with padding	"hi".rjust(5) → " hi"
str.center()	Center-align with padding	"hi".center(5) → " hi "

**5. Advanced Methods**
Method	Description	Example
str.encode()	Convert to bytes (e.g., UTF-8)	"hi".encode() → b'hi'
str.maketrans()	Create translation table (for translate())	str.maketrans("a", "x")
str.translate()	Replace characters using a translation table	"abc".translate(table)
str.partition()	Split into 3 parts at first occurrence	"a,b,c".partition(",") → ("a", ",", "b,c")
str.rpartition()	Split into 3 parts at last occurrence	"a,b,c".rpartition(",") → ("a,b", ",", "c")


**6. Practical Examples**
Example 1: Clean User Input
python
user_input = "  Hello, World!  "
cleaned = user_input.strip().lower()  # → "hello, world!"
Example 2: Check for Numeric Input
python
if user_input.isdigit():
    print("Valid number!")
Example 3: Split CSV Data
python
csv_data = "a,b,c,d"
items = csv_data.split(",")  # → ["a", "b", "c", "d"]
Example 4: Dynamic Formatting
python
name, age = "Alice", 30
print(f"{name} is {age} years old.")  # → "Alice is 30 years old."


**7. Key Takeaways**
Case Conversion: Use lower(), upper(), title() for consistent formatting.

Searching: find(), startswith(), and count() are faster than regex for simple checks.

Cleaning: strip(), replace(), and split() are essential for data preprocessing.

Validation: isalpha(), isdigit(), and isalnum() help sanitize inputs.