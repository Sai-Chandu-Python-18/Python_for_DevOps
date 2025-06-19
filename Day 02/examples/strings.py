# string concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

# len function in string
text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

#lower and Upper cases
text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#replace() method in string
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

#split() method in string
text = "Python is awesome"
words = text.split()
print("Words:", words)

#strip() method in string
text = "   Some spaces around   "
stripped_text = text.strip()
print("Stripped text:", stripped_text)

#substring in string
text = "Python is awesome"
substring = "is"
if substring in text:
    print(substring, "found in the text")
else:
    print(substring,"Not found in the text")
    
    
#count() method in string
text="python programming"
count_str=text.count("o")
print("Count of o:",count_str)


#join the string
text="Python is Awesome"
new_text="-->".join(text)
print("new text :",new_text)


#find() method in string

text="Python is high level language"
print(text.find("h"))

#format() string

var1-="Sai Chandu"
var2="Vaddla"
print("My name is {} nad my last name is {}".format(var1,var2))

#isalnum() method in string
text="chandu123"
print(text.isalnum())

digit="1243536"
print(digit.isdigit())

alpha="SaiChandu"
print(alpha.isalpha())



#upper(),lower(),capitalize(),title(),swapcase()
text="Programming language"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

#index(),rindex(),find(),rfind() methods in string

text="Python is a High leven programming language"
print(text.index("a"))
print(text.rindex("i"))
print(text.find("a"))
print(text.rfind("a"))

#startswith(),endswith() methods in string

text="Programming language"
print(text.startswith("P"))
print(text.endswith("e"))



