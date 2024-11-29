"""
write data to a text file
"""

line = "This is a new text file"

with open('newfile.txt', 'w') as f:
    f.write(line)
