/*

Anchors
Description

Write a regular expression that matches any string that starts with one or more ‘1’s, followed by three or more ‘0’s, followed by any number of ones (zero or more), followed by ‘0’s (from one to seven), and then ends with either two or three ‘1’s.

Execution Time Limit
15 seconds

*/



import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "^1+0{3,}1*"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
