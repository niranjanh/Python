/*

Grouping

Description
You have a string which contains a data in the format DD-MM-YYYY. Write a regular expression to extract the date from the string.

Sample input:
"Today’s date is 18-05-2018."

Sample output:
18-05-2018

Execution Time Limit
10 seconds

*/


import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "((\d{2})\-(\d{2})\-(\d{4}))"

# store result
result = re.search(pattern, string)  # pass the parameters to the re.search() function

if result != None:
    print(result.group(0))  # result.group(0) will output the entire match
else:
    print(False)
