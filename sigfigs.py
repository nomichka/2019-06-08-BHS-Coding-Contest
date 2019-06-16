#READING
import os
path="sigfigs.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

for i in range(N):
    if "\n" in lines[i]:
        lines[i]=lines[i][0:len(lines[i])-1]
    num=lines[i]
    while num[0]=="0":
        num=num[1:]
    if "." not in num:
        while num[len(num)-1]=="0":
            num=num[0:len(num)-1]
    else:
        ind=num.index(".")
        num=num[0:ind]+num[ind+1:]
    print(len(num))
