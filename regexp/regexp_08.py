/*

Quantifiers

Description
Check that the pattern ‘ab+’ will not match the string ‘ac’. 


You can also play around with the '+' quantifier by using it to match different types of strings.

Execution Time Limit
15 seconds

*/



import re

# input string
string = "ac"

# regex pattern
pattern = "ab+"

# check whether pattern is present in string or not
result = re.search(pattern, string)

# print result
if result != None:
    print(True)
else:
    print(False)
