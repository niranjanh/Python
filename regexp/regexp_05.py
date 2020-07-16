/*

Quantifiers
Description
Write a regular expression that matches the following words: 
xyz 
xy 
xz 
x 

Make sure that the regular expression doesn’t match the following words: 
Xyyz 
Xyzz
Xyy 
Xzz 
Yz 

Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "xy?z?"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
