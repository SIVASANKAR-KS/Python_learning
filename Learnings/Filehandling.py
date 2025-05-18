import os
f=open("demofile.txt", "a")
f.write("Please check the lines")
f.close()
f=open("demofile.txt", "rt")
#print(f.read(7))                    #==> reads 3 characters
'''print(f.readline())
print(f.readline())                  #==> evertime you use read or read line, the file pointer will be moved
print(f.readline())'''
#print(f.readlines())                # prints entire file into list echa line as an element
#print("print lines of file")
for x in f:
    print(x)
f.close()
#os.mkdir("sdks")
os.rmdir("sdks")
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("File does not exist")