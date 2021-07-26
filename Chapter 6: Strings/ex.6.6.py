"""
Exercise 6: Experiment with strip and replace
"""

str = '   spacious   '
# Use .lstrip, .rstrip, and .strip
print(str.lstrip() + "\n" + str.rstrip() + "\n" + str.strip())

str2 = 'hello world!'
print(str2)
# Use .replace
replaced_str2 = str2.replace('hello', 'hi')
# Output replaces word, but not rest of string
print(replaced_str2)
