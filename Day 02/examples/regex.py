#findall() methods in regular expressions
import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
    
#match() method in regular expressions
text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")
    
#split() method in regular expressions
text = "apple,banana,orange,grape"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)

#sub() method in regular expressions
text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)

#search() method in regular expressions
text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")
    
#finditer() method in regular expressions
text="The quick brown for jumps over the lazy brown dog"
pattern=r"brown"
for match in re.finditer(pattern,text):
    print("Pattern found:".match.group())
    
else:
    print("Pattern Not found")
    
#compile() method in regular expressions
text="The quick brown for jumps over the lazy brown dog" 
pattern=r"quick"
compiled_pattern =re.compile(text)
if compiled_pattern.search(text):
    print("pattern found")
else:
    print("pattern not found")
    
#match() method in regular expressions
text="The quick brown for jumps over the lazy brown dog" 
pattern=r"quick"
if re.match(pattern,text):
    print("Pattern found")
else:
    print("pattern not found")
    
#Extract Phone Numbers
text = "Call me at 123-456-7890 or 987-654-3210"
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(phones)  # Output: ['123-456-7890', '987-654-3210']

#Checking The Email_address or Validating the email
email = "user@example.com"
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Valid email!")
 
#Replacing the Dates
text = "Today is 12/25/2023"
new_text = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2', text)
print(new_text)  # Output: "Today is 2023-12-25"
    