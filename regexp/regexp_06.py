/*

Quantifiers

Description
Match a binary number that starts with 101 and ends with zero or more number of zeroes. 

Sample positive cases (pattern should match all of these): 
1010 
10100 
101000 
101 

Sample negative cases (shouldn’t match any of these): 
10 
100 
1
Execution Time Limit
15 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "1010*"

# check whether pattern is present in string or not
result = re.search(pattern, string)

# evaluate result - don't change the following piece of code, it is used to evaluate your regex
if result != None:
    print(True)
else:
    print(False)
