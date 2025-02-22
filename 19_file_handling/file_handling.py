f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>


f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()


f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()


f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()


f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()


f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()


with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')


with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')


import os
os.remove('./files/example.txt')


import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')