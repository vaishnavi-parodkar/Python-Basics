import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200


print("to print something we use this format")

name = "Alice"
age = 25
print(name) 
name = "Dave"

print(name) 
print(age)

# single line comment

"""
this is multi-line comment
"""
 
print(5+5)

numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

total = sum(numbers)
print(f"Total: {total}")

#string
string = "My Name is XYZ"

long_string = """
multi-line string
written in this format
"""
first_name = "ABC"
last_name = "XYZ"
full_name = first_name + " " + last_name

long_dash = "-"*12
print(full_name)
print(long_dash)

len(long_dash)

message = "Hello"
print(message + " World!")
message = message.upper()
print(message)

is_true = True # true is wrong it should be capital T
has_license = True

age = 18
can_vote = age>=18
print(can_vote)
is_18 = age==18

can_drive = age >= 16 and has_license 
print(can_drive) 


# String manipulation
#fstring

namef="Riya"
string = f"Hi, my name is {namef}!"

#string methods
namef.lower()
namef.upper()

sentence="hi my name is XYZ"
sentence.title()

# control flow
# if, if-else, if-else ladder

temp = 25
if temp > 30:
    print("It's very hot")
elif temp >25:
    print("It's hot")
else:
    print("It's not hot")

# for loop
for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(0,10,2):
    print(i)

# Data Structures
# 1. Lists
# 2. Dictionaries
# 3. Tuples
# 4. Sets


# Lists
my_list = ["Alice", 25, age, True, has_license]
name_alice = my_list[0]
age = my_list[1]
has_license=my_list[-2]

# Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
person["name"] = "Diya"
person["licence"]=True
del person["licence"]


# empty tuple
empty = ()
#  Tuples with items
point = (3,5)
colors = ("red","green","blue")
# colors[0]="black" gives error 


# Sets
# empty set 
empty_set = set()

# set with values 
numbers_set={1,2,3,4,5}
fruits_set=(["apple","banana","orange"])

# From list (removes duplicates)
scores_list=[85,90,85,92,90]
unique_scores = set(scores_list)


