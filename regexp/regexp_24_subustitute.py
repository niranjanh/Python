/*


The 're.sub()' function

Description
You are given the following string: 

“You can reach us at 07400029954 or 02261562153 ”
 
Substitute all the 11-digit phone numbers present in the above string with “####”. 

Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "\d{11}"

# replacement string
replacement = "####"

# check whether pattern is present in string or not
result = re.sub(pattern, replacement, string)

if (re.search(replacement, result)) != None:
    print(True)
else:
    print(False)
