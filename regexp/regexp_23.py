/*

The 'Match' Function

Description
Write a string such that when you run the re.match() function on the string using the given regex pattern 'a{2,}' , the function returns a non-empty match.

Execution Time Limit
10 seconds

*/



import re
import ast, sys
pattern = sys.stdin.read()

# write a string such that the re.match() function returns a non-empty match while using the pattern 'a{2,}' 
string = "aabbbbbb"

# check whether pattern is present in string or not
result = re.match(pattern, string, re.I)

if (result != None):
    print(True)
else:
    print(False)
