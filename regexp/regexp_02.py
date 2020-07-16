/*

Regular Expressions
Description
Consider the same problem as the previous question.  Extract the word 'education' from the sentence  'The roots of education are bitter, but the fruit is sweet'. But this time, extract the starting position of the result using result.start().

*/

# import the regular expression module
import re

# input string on which to test regex pattern
string = 'The roots of education are bitter, but the fruit is sweet.'

# regular expression pattern to check if 'education' is present in a given string or not.
pattern = 'education'

# store the match of regex
result = re.search(pattern, string)

# store the start of the match
# use result.start()
start_position = result.start()

print(start_position)
