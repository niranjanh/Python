/*

Quantifiers
Description
Write a regular expression which matches variants of the word ‘awesome’ where there are more than two ‘e’s at the end of the word. 

The following strings should match: 
Awesomeee 
awesomeeee 

The following strings shouldn’t match: 
Awesom 
Awesome 
Awesomee 

Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "a?A?wesome{3,}"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
