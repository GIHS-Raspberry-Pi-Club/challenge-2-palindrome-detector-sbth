# Regex.
import re

# As per README, palindromes can have numbers or letters, and ignore
# spaces and punctuation.
s = re.sub('[^a-z0-9]', '', input('Enter a string: ').lower())

# Print results of comparing s with itself backwards.
print(s == s[::-1])

