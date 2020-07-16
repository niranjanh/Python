/*


Quantifiers

Description
Write a pattern that starts with 1 and ends with zero but has arbitrary number of 1s (zero or more) in between

Sample positive cases (should match all of these):
110 
11111110 
10 

Sample negative cases (shouldn't match any of these): 
11 
00 
1 
0


Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "11*0"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
