/*

Comprehension: Pipe Operator

Description

Write a regular expression that matches the following strings: 

Basketball 
Baseball 
Volleyball 
Softball 
Football


Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "(Basket|Volley|Soft|Base|Foot)ball"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
