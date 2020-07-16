/*

Quantifiers

Description
Write a regular expression that matches the word ‘tree’ or ‘trees’ in a given piece of text. 

Sample positive cases:
‘The tree stands tall.’ 
‘There are a lot of trees in the forest.’ 

Negative negative cases: 
‘The boy is heading for the school.’ 
'It's really hot outside!'

Execution Time Limit
10 seconds

*/


import ast, sys
string = sys.stdin.read() # input string

# import the regular expression module
import re

# regex pattern
pattern = "trees?"

# check whether pattern is present in string or not
result = re.search(pattern, string)  # pass the arguments to the re.search function

if result != None:
    print(True)
else:
    print(False)
