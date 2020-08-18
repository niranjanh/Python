/*

The 're.finditer()' function

Description
Write a regular expression to extract all the words from a given sentence. Then use the re.finditer() function and store all the matched words that are of length more than or equal to 5 letters in a separate list called result.

Sample input:
"Do not compare apples with oranges. Compare apples with apples"

Expected output:
6

Execution Time Limit
10 seconds


*/

import re
import ast, sys
string = sys.stdin.read()

# regex pattern
pattern = "\w{5,}"

# store results in the list 'result'
result = []

# iterate over the matches
for match in re.finditer(pattern, string):
    if len(match.group()) >= 5:
        result.append(match)
    else:
        continue

print(len(result))
