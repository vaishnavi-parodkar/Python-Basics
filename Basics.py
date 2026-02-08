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