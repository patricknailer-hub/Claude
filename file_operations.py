# Creating/writing to a file
with open('my_file.txt', 'w') as f:
    f.write('This is my content')

# Reading from a file
with open('my_file.txt', 'r') as f:
    content = f.read()
    print(content)

# Listing files
import os
files = os.listdir('.')
print(files)
