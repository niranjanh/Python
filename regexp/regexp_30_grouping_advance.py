/*

Groups

Description
Write a regular expression to extract the domain name from an email address. The format of the email is simple - the part before the ‘@’ symbol contains alphabets, numbers and underscores. The part after the ‘@’ symbol contains only alphabets followed by a dot followed by ‘com’ 
 
Sample input: 
user_name_123@gmail.com 
 
Expected output: 
gmail.com

Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "([\w_]+)@([a-zA-Z]+\.com)"

# store result
result = re.search(pattern, string)

# extract domain using group command
if result != None:
    domain = result.group(2)
else:
    domain = "NA"

print(domain)
