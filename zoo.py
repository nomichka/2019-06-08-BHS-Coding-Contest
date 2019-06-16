#READING
import os
path="zoo.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

a=""
for i in range(N):
    lines[i]=lines[i].split()
    lines[i][0]=int(lines[i][0])
for i in range(len(lines)):
    toRemove=[]
    for j in range(i + 1, len(lines)):
        if lines[i][1]==lines[j][1]:
            lines[i][0]+=lines[j][0]
            toRemove.append(lines[j])
    for j in toRemove:
        lines.remove(j)


for i in range(len(lines)):
    a+=str(lines[i][0])+" "+lines[i][1]+" "
print(a)

