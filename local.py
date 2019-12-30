import os

path = 'C:\\Users\\MABDIN\\.ssh\\config'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.txt' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)

f = open(path, 'r')
print(f.read())
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

