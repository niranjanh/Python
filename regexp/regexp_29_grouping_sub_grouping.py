/*

Grouping

Description
In the last exercise, you had extracted the date from a given string. In this coding exercise, write the same regular expression. But this time, use grouping to extract the month from the date. The expected date format is DD-MM-YYYY only.

Sample input: 
Today's date is 18-05-2018
 
Expected output: 
05

Execution Time Limit
10 seconds

*/

import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "((\d{2})\-(\d{2})\-(\d{4}))"

# store result
result = re.search(pattern, string)

# extract month using group command
if result != None:
    month = result.group(3)
else:
    month = "NA"

print(month)
