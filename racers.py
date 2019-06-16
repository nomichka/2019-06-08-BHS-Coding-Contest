#READING
import os
path="racers.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

a=""
def my_function(entry):
    return (entry[1])
for i in range(N):
    lines[i]=lines[i].split()
    lines[i][1]=float(lines[i][1])
lines=sorted(lines, key=my_function)
for i in range(N):
    a+=lines[i][0]+" "
print(a)
