print("YES")



#READING
import os
path="cipher.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])-1
lines.remove(lines[0])

a="abcdefghijklmnopqrstuvwxyz"

for i in range(N):
    yes=True
    lines[i]=lines[i].split()
    for j in range(len(lines[i][0])):
        if lines[i][0][j]=="a":
            lines[i][0]=lines[i][0][0:j]+"z"+lines[i][0][j+1:]
        else:
            lines[i][0]=lines[i][0][0:j]+a[a.index(lines[i][0][j])-1]+lines[i][0][j+1:]
    for j in range(len(lines[i][0])):
        if lines[i][0][j] not in lines[i][1]:
            print("NO")
            yes=False
            break
        else:
            lines[i][1]=lines[i][1][0:lines[i][1].index(lines[i][0][j])]+lines[i][1][lines[i][1].index(lines[i][0][j])+1:]
    if yes:
        print("YES")











