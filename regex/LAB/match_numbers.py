import re
numbers = input()

pattern = r'(^|(?<=\s)-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s)))'