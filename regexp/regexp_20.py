/*

Meta-sequences

Description
Write a regular expression with the help of meta-sequences that matches usernames of the users of a database. The username starts with alphabets of length one to ten characters long and then followed by a number of length 4.

Sample positive matches:
sam2340 
irfann2590 

Sample negative matches:
8730 
bobby9073834 
sameer728 
radhagopalaswamy7890 

Execution Time Limit
10 seconds

*/



import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "^\w{1,10}\d{4}"

# check whether pattern is present in string or not
result = re.search(pattern, string, re.I)

if result != None:
    print(True)
else:
    print(False)
