# Regex.
import re

# As per README, palindromes are made up of letters and numbers, and ignore
# punctuation and spacing.
s = re.sub('[^0-9a-z]', '', input('Enter a string: ').lower())

# Compare s to itself reversed, print bool result..
print(s == s[::-1])

