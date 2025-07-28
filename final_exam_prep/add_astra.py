import re

information = input()
pattern = r'([#|])([A-Za-z\s]+)(\1)(\d{2}\/)(\d{2}\/)(\d{2})\1(\d+)\1'
matches = re.findall(pattern, information)