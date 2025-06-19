# Regex

**1. Regular Expressions for Text Processing:**

- Regular expressions (regex or regexp) are a powerful tool for pattern matching and text processing.
- The `re` module in Python is used for working with regular expressions.
- Common metacharacters: `.` (any character), `*` (zero or more), `+` (one or more), `?` (zero or one), `[]` (character class), `|` (OR), `^` (start of a line), `$` (end of a line), etc.
- Examples of regex usage: matching emails, phone numbers, or extracting data from text.
- `re` module functions include `re.match()`, `re.search()`, `re.findall()`, and `re.sub()` for pattern matching and replacement.

**Regular Expressions (Regex) in Python**
Regular expressions are powerful tools for pattern matching and text manipulation. Python's re module provides regex support. Here's a structured guide:

**1. Basic Regex Syntax**
Pattern	Matches	Example
.	Any character (except newline)	a.c → "abc", "a1c"
\d	Digit (0-9)	\d\d → "42"
\w	Word character (a-z, A-Z, 0-9, _)	\w+ → "Hello_123"
\s	Whitespace (space, tab, newline)	\s+ → " "
^	Start of string	^Py → "Python"
$	End of string	thon$ → "Python"
*	0+ repetitions	a* → "", "a", "aa"
+	1+ repetitions	\d+ → "1", "123"
?	0 or 1 repetition	colou?r → "color", "colour"
{n}	Exactly n repetitions	\d{3} → "123"
[abc]	Any of a, b, or c	[aeiou] → "e" in "hello"
( ... )	Capture group	(\d{3}) → "123" in "ID: 123"

**2. Python re Module Methods**
Common Functions
python
import re
Method	Purpose	Example
re.search()	Find first match anywhere in the string	re.search(r'\d+', "ID: 123")
re.match()	Find match only at the string's start	re.match(r'Py', "Python")
re.findall()	Return all matches as a list	re.findall(r'\d+', "1a22b333") → ['1', '22', '333']
re.sub()	Replace matches with a string	re.sub(r'\d+', '#', "1a22b") → "#a#b"
re.split()	Split string by regex pattern	re.split(r'\s+', "Hello World") → ['Hello', 'World']


**3. Practical Examples**
Example 1: Extract Phone Numbers
python
text = "Call me at 123-456-7890 or 987-654-3210"
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(phones)  # Output: ['123-456-7890', '987-654-3210']
Example 2: Validate Email Addresses
python
email = "user@example.com"
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Valid email!")
Example 3: Replace Dates
python
text = "Today is 12/25/2023"
new_text = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', text)
print(new_text)  # Output: "Today is 2023-12-25"

**4. Advanced Features**
Named Groups
python
text = "Name: John, Age: 30"
match = re.search(r'Name: (?P<name>\w+), Age: (?P<age>\d+)', text)
print(match.group('name'))  # Output: "John"
print(match.group('age'))   # Output: "30"
Non-Greedy Matching
python
text = "<b>Hello</b> <i>World</i>"
matches = re.findall(r'<.*?>', text)  # `?` makes it non-greedy
print(matches)  # Output: ['<b>', '</b>', '<i>', '</i>']
Flags
python
# Case-insensitive search
re.findall(r'python', 'Python is fun', re.IGNORECASE)  # Output: ['Python']


**5. Common Use Cases**
Data Cleaning: Remove unwanted characters (e.g., re.sub(r'[^\w\s]', '', text)).

Log Analysis: Extract timestamps or error codes.

Web Scraping: Parse HTML/XML (use with caution; prefer tools like BeautifulSoup).

**6. Tools & Resources**
Regex Tester: regex101.com

Cheat Sheet: Python Regex Cheatsheet

Key Takeaways
Use re.search()/re.findall() for extraction.

re.sub() is ideal for replacements.

**Raw strings (r'...'**) prevent escaping issues (e.g., r'\d'vs'\d'`).

Practice regex with real-world datasets (e.g., logs, emails) to master it!