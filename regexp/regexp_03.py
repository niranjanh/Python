/*

Regular Expressions

Description

Consider the same problem as described in the first question. Extract the word 'education' from the sentence 'The roots of education are bitter, but the fruit is sweet'. But this time extract the ending position of the match using result.end().

Execution Time Limit
10 seconds

*/


# import the regular expression module
import re

# input string
string = 'The roots of education are bitter, but the fruit is sweet.'

# write a regular expression pattern to check if 'education' is present in a given string or not.
pattern = 'education'

# store the match of regex
result = re.search(pattern, string)

# store the end of the match using result.end()
end_position = result.end()

print(end_position)
