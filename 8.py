# Python Strings
print("Hello")
print('Hello')

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
 
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Slicing Strings
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

# Modify Strings
# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
# The lower() method returns the string in lower case:

a = "Hello, World!"
print(a.lower())

# he strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#String Concatenation
#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)
#Format - Strings
#Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)
#isplay the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#Escape Characters
#The escape character allows you to use double quotes when you normally would not be allowed:

txt = "We are the so-called \"Vikings\" from the north."

