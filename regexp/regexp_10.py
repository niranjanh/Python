/*

Quantifiers

Description
Write a regular expression to match the word ‘hurray’. But match only those variants of the word where there are a minimum of two ‘r’s and a maximum of five ‘r’s.

Execution Time Limit
10 seconds

*/

import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "hur{2,5}ay"

# check whether pattern is present in string or not
result = re.search(pattern, string)  # pass the pattern and string arguments to the function

if result != None:
    print(True)
else:
    print(False)
