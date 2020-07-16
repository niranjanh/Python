/*

Comprehension: Escape Sequence

Description
Write a regular expression that returns True when passed a multiplication equation. For any other equation, it should return False. In other words, it should return True if there an asterisk - ‘*’ - present in the equation. 

Sample positive cases (should match all of these):
3a*4b 
3*2 
4*5*6=120 

Sample negative cases (shouldn't match either of these):
5+3=8 
3%2=1

Execution Time Limit
10 seconds

*/


import re

import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = ".\*."

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
