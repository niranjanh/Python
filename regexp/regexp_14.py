/*

Comprehension: Grouping

Description
Write a regular expression which matches a string where '23' occurs one or more times followed by occurrence of '78' one or more times

Sample positive matches (should match all of these):
2378
23237878
232323237878

Sample negative matches (shouldn't match either of these):
23
78
23378
223378
22337788

Execution Time Limit
10 seconds

*/

import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "(23)+(78)+"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
