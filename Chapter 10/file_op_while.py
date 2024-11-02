f = open("Chapter 10/write.txt")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()