/*

Regular Expressions
Description
Consider the following sentence: "The roots of education are bitter, but the fruit is sweet.".

Write a regular expression pattern to check whether the word ‘education’ is present in the given string or not. Use the re.search() function.


*/

# import the regular expression module
import re

# input string on which to test regex pattern
string = 'The roots of education are bitter, but the fruit is sweet.'

# regex pattern to check if 'education' is present in a input string or not.
pattern = "education"

# check whether pattern is present in string or not
result = re.search(pattern, string)

if result != None:
    print(True)
else:
    print(False)
