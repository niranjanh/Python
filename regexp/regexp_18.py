/*


Anchors

Description
Write a pattern which matches a word that ends with ‘ing’. Words such as ‘playing’, ‘growing’, ‘raining’, etc. should match while words that don’t have ‘ing’ at the end shouldn’t match.

Execution Time Limit
10 seconds

*/


# 15_1

import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = ".(ing)$"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
