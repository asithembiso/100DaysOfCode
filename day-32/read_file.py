"""
Read and display contents of a text file
"""
import os


cwd = os.getcwd()

with open(cwd + '/myfile.txt') as f:
    print(f.read())
