/*


Quantifiers

Description
Write a pattern that matches numbers that are power of 10.


Sample positive matches (should match all of the following):
10
100
1000


Sample negative matches (shouldn't match either of these):
0
1
15

Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "10+"

# check whether pattern is present in string or not
result = re.search(pattern, string) 

if result != None:
    print(True)
else:
    print(False)
