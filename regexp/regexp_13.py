/*


Quantifiers
Description
Write a regular expression to match a term that has three or more ‘0’s followed by one or more ‘1’s

Sample positive matches (should match all of these):
0001 
000001111 
000011 

Negative positive matches (shouldn't match either of these):
00111 
000 
00 
111
Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "0{3,}1+"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
