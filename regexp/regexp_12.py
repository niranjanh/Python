/*


Quantifiers
Description
Write a regular expression that matches the a string where ‘a’ is followed by ‘b’ a maximum of three times.

Sample positive matches (should match all of these):
a
ab
abb
abbb

Sample negative matches (shouldn't match either of these):
abbbb
abbbbbbbb
Execution Time Limit
10 seconds


*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "ab{0,3}"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
