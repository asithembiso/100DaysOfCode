"""
Append data to an existing text file
"""

line = "This is appended line"

with open('newfile.txt', 'a+') as f:
    f.write('\n' + line)
