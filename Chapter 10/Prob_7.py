line = 1

with open("Chapter 10/log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"The word 'python' is found in the log file. Line no. :{lineno}")
        break
    lineno += 1

else:
    print("The word 'python' is not found in the log file.")

#for with else