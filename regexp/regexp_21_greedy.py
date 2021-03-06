/*
Greedy Search

Description
You’re given the following html code: 

<html> 
<head> 
<title> My amazing webpage </title> 
</head> 
<body> Welcome to my webpage! </body> 
</html> 

Write a greedy regular expression that matches the entire code.

Execution Time Limit
10 seconds


*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "<.*>"

# check whether pattern is present in string or not
result = re.search(pattern, string, re.M)  # re.M enables tha tpettern to be searched in multiple lines

if (result != None) and (len(result.group()) > 6):
    print(True)
else:
    print(False)
