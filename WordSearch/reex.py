# Python program to illustrate
# Matching regex objects
import re
phoneNumRegex = re.compile(r'OF')
mo = phoneNumRegex.search('My number is WOOFY')
print(mo.group())