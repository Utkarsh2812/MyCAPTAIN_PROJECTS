import os

s = input('Enter file name with extension ') 
file = os.path.splitext(s)
print(file[1])

