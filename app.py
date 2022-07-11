#Strings
"I'm a string"
'Me too'
str("I'm a string")

dog_name = "Lucy"
print(f"Say hello to my dog {dog_name}")

price_1 = 3
price_2 = 2.5
print(f"Item 1 costs ${price_1:.2f}")
print(f"Item 2 costs ${price_2:.2f}")

"hello" # hello
"hello".upper() # "HELLO"
"HELLO".lower() # "hello"
"hello".capitalize() # "Hello"
"hello" + "world" # "helloworld"
"hello" * 3 # "hellohellohello"

type("hello") # <class 'str'>

dir("hello") # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', ... ]

#print(dir("hello"))

#Numbers
int("1")
# 1
int(float("1.1"))
# 1
float("1.1")
# 1.1

4 / 3
# 1.3333333333333333
4 / 3.0
# 1.3333333333333333
int(4/3)
# 1
float(4 / 3)
# 1.3333333333333333

print(float(4/3))

# Lists
[1, 3, 400, 7]
list() #[]

list_abc = ['a', 'b', 'c']
list[0] #'a'
list[1] #'b'
list[2] #'c'

len([1, 3, 400, 7]) #4 (the length of the list)
sorted([5, 100, 234, 7, 2])
# [2, 5, 7, 100, 234]
list_123 = [1, 2, 3]
list_123.pop()
# 3
list_123.remove(1)
print(list_123)
# [2]

#Tuples
(1, 2, 3)
# (1, 2, 3)
tuple([1, 2, 3])
# (1, 2, 3)

#Sets
first_set = set()
# {}

empty_set = {}
print(first_set)
print(empty_set)
#set(3, 2, 3, 'a', 'b', 'a')
# TypeError: set expected at most 1 argument, got 6

set([3, 2, 3, 'a', 'b', 'a'])
# {2, 3, 'a', 'b'}

#Dictionaries
{ "key1": "value1", "key2": "value2" }

my_dict = { "key1": 1, "key2": 2 }
my_dict["key2"]
# 2

my_dict = { "key1": "value1", "key2": "value2" }
#print(my_dict["key3"])
# KeyError: 'key3'

print(my_dict.get("key3"))
# None

my_dict = { "key1": "value1", "key2": "value2" }
#my_dict.key2
# AttributeError: 'dict' object has no attribute 'key2'

dict(x = 1, y = 2)
# {'x': 1, 'y': 2}

# None

#no_value
# NameError: name 'no_value' is not defined

no_value = None
print(no_value)
# None

# Booleans

type(True)
# <class 'bool'>
type(False)
# <class 'bool'>

not True
# False
not False
# True
not 1
# False
not 0
# True
not ''
# True
not None
# True
not []
# True
not ()
# True
not {}
# True
