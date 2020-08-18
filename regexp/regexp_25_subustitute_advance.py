/*

The 're.sub' function

Description
Write a regular expression such that it replaces the first letter of any given string with ‘$’. 

For example, the string ‘Building careers of tomorrow’ should be replaced by “$uilding careers of tomorrow”.

Execution Time Limit
10 seconds


*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "\w{1}?"

# replacement string
replacement = "$"

# check whether pattern is present in string or not
result = re.sub(pattern, replacement, string)  # pass the parameters to the sub function

print(result[0] == '$')
