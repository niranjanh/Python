/*

Anchors

Description
Write a pattern that matches all the dictionary words that start with ‘A’

Positive matches (should match all of these): 
Avenger 
Acute 
Altruism 

Negative match (shouldn’t match any of these): 
Bribe 
10 
Zenith

Execution Time Limit
10 seconds

*/

import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "^A+"

# check whether pattern is present in string or not
result = re.search(pattern, string, re.I)  # re.I ignores the case of the string and the pattern

if result != None:
    print(True)
else:
    print(False)

