

# unicode examples, \u \N

a = 'Hello'
c = 'it\'s Monday'
a = '\u265E'
b = '\N{ROMAN NUMERAL NINE}'

print(a)
print(b)
print(c)

# escape symbol

# string type, raw example

d = r"It's Monday"
print(d)

# converts: capitalize(), lower(), upper(), swapcase(), title()

a = "asdDDFqwe"
print(a.capitalize())

# checks: startwith(), endwith(), isalnum(), isalpha(), isdigit(), isspace(), istitle(), isupper(), islower()

a = "Hi how are you"
print(a.startswith('H'))

# modify methods:
# replace()
a = "Hi how are you"
b =  a.replace('Hi', 'Hello')
print(b)

# split
a = "Hi how are you"
for i in a.split('o'):
    print(i)

# join()

a = ['a', 'b', 'c']
print(':'.join(a))

import os
os.path.join('c:', 'Users', 'Rufat_Feyzullayev')

# format
# concatenation

a = 'it is '
b = 'Monday'
c = 'Friday'

print(a + b)

print("it is %s but not %s today" % (b, c))
print("it is {0}, definitely {0} but not {1} today".format(b, c))
print(f"it is {b}, definitely {b} but not {c} today")

#regexp

import re

a = "It is Monday and it is good day"
result = re.search(r'M.*?day', a)
print (result.group())

print (re.findall(r'(.*t) is', a, re.IGNORECASE))