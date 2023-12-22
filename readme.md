> [test](https://coal-spell-50a.notion.site/Cyberzz-6144b9c5f5fd4ca99f205e31925d7a57?pvs=4). Just trying out markdown syntax!

> [another small test](https://github.com/Mircodj/C0D1C3-X-L0R1S-B0RR4T4)
 
> [yy](https://luminous-picture-b9d.notion.site/lordhavemercy-1-da89d647915b4b9998580ee40479a2ef)
# Variables and data types
| Data Type | Description | Syntax |
| --- | --- | --- |
| Integer | Whole numbers | `x = 10` |
| Float | Decimal numbers | `x = 10.0` |
| String | Sequence of characters | `x = "Hello"` |
| Boolean | True or False values | `x = True` |

| Data Type | Description | Syntax | Ordered | Changeable | Allows Duplicates | Indexed |
| --- | --- | --- | --- | --- | --- | --- |
| Dictionary | Collection of key-value pairs | `mydict = {"key": "value"}` | No | Yes | No (for keys) | Yes |
| List | Collection of items | `mylist = ["item1", "item2"]` | Yes | Yes | Yes | Yes |
| Set | Collection of unique items | `myset = {"item1", "item2"}` | No | Yes | No | No |
| Tuple | Collection of items | `mytuple = ("item1", "item2")` | Yes | No | Yes | Yes |

Lists are the ones i'll probably use the most

```python
#List of some different variable types:
x = 123      # integer
x = 123L     # long integer
x = 3.14      # double float
x = "hello"       # string
x = [0,1,2]       # list
x = (0,1,2)       # tuple
x = open(‘hello.py’, ‘r’)  # file
```

# Strings and functions
```python
x = "Hello World"

```

Functions:
| Function | Description | Syntax |
| --- | --- | --- |
| len() | Returns the length of a string | `len(x)` |
| lower() | Converts a string to lower case | `x.lower()` |
| upper() | Converts a string to upper case | `x.upper()` |
| replace() | Replaces a string with another string | `x.replace("old", "new")` |
| split() | Splits a string into substrings | `x.split("delimiter")` |
| join() | Joins a list of strings into one string | `"delimiter".join(list)` |
| find() | Returns the index of the first occurrence of a substring | `x.find("substring")` |
| count() | Returns the number of times a substring occurs in a string | `x.count("substring")` |
Up until join they are actually useful. Note that there are many more.

Concatenation: 
```python
print "You can concatenate two " + "strings with the '+' operator."
 
str1 = "Hello"
str2 = "World"
str1 + str2    	# concatenation: a new string

# String literals may be concatenated by a space
word = 'left' "right" 'left'

# Any string expression may be concatenated by a +
word = wordA + " " + wordB
```

# Operators
| Operator | Description | Syntax |
| --- | --- | --- |
| + | Addition | `x + y` |
| - | Subtraction | `x - y` |
| * | Multiplication | `x * y` |
| / | Division | `x / y` |
| % | Modulus | `x % y` |
| ** | Exponentiation | `x ** y` |
| // | Floor division | `x // y` |
| == | Equal | `x == y` |
| != | Not equal | `x != y` |
| > | Greater than | `x > y` |
| < | Less than | `x < y` |
| >= | Greater than or equal to | `x >= y` |
| <= | Less than or equal to | `x <= y` |
| and | Logical AND | `x and y` |
| or | Logical OR | `x and y` |
| not | Logical NOT | `not x` |
| is | Object identity | `x is y` |
| is not | Negated object identity | `x is not y` |
| in | Membership test | `x in y` |
| not in | Negated membership test | `x not in y` |

# For loops and iteration
```python
for i in range(5):
    print(i)

browsers = ["Safari","Firefox","Chrome"]
for browser in browsers:
    print browser
```


# List
Lists in Python are a collection of items, such as Strings, Integers or other Lists.
Lists are enclosed in [ ] with each item separated by commas.
Lists, unlike Strings are mutable, which means they can be changed.
```python
emptyList = []
bourbonList = ['jeffersons','woodford reserve','maker's mark']
numList = [1,2,3,4]
mixedList = ['hello', 2, 3.14, True]
```

Functions:
| Function | Description | Syntax |
| --- | --- | --- |
| len() | Returns the length of the list | `len(list)` |
| append() | Adds an element at the end of the list | `list.append(x)` |
| extend() | Adds all elements of a list to another list | `list.extend(iterable)` |
| insert() | Adds an element at a specified position | `list.insert(i, x)` |
| remove() | Removes the first item with the specified value | `list.remove(x)` |
| pop() | Removes the element at the specified position | `list.pop([i])` |
| clear() | Removes all the elements from the list | `list.clear()` |
| index() | Returns the index of the first element with the specified value | `list.index(x)` |
| sort() | Sorts the list | `list.sort()` |
| reverse() | Reverses the order of the list | `list.reverse()` |
| copy() | Returns a copy of the list | `list.copy()` |
| count() | Returns the number of elements with the specified value | `list.count(x)` |

# Dictionary
Dictionaries in Python are a collection of key-value pairs.
Dictionaries are enclosed in { } with each item separated by commas.
Dictionaries are unordered, which means they can't be sorted.
```python
# This is a list
myList = ["first","second","third"]

# This is a dictionary
myDictionary = {0:"first",1:"second",2:"third"} 
```

# Type conversion
```python
# Convert to integer
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Convert to float
x = float(1)     # x will be 1.0

# Convert to string
x = str(1)    # x will be '1'
y = str(2.8)  # y will be '2.8'

# Convert to boolean
x = bool(1) # x will be True

# Convert to list
x = list((1,2,3)) # x will be [1,2,3]
```

# Input
```python
# Get user input
name = input("Enter your name: ")
print("Hello, " + name)
```


# Quirks:
- input always returns strings, convert it as needed!


# Stuff
SQL Inj: `' OR '1'='1`


# Snippets
```python
def XORdecode(message, KEY="c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored
	
def base64decode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64decode(message_bytes) # i changed it here to decode (took me a while)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

def base32decode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32decode(message_bytes) # here too
    b32_message = b32_bytes.decode('ascii')
    return b32_message

def ROTencode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i+pos)%LEN]
    return rot13_enc
```
