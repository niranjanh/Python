/*

The 're.findall()' function

Description
Write a regular expression to extract all the words that have the suffix ‘ing’ using the re.findall() function. Store the matches in the variable ‘results’ and print its length.

Sample input:
"Playing outdoor games when its raining outside is always fun!"

Expected output:
2

Execution Time Limit
10 seconds


*/

import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "ing"

# store results in the list 'result'
result = []

for match in re.findall(pattern, string):
    result.append(match)

print(len(result))
