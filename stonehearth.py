#READING
import os
path="stonehearth.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

for i in range(N):
    possibilities=[]
    health=int(lines[i*2])
    minions=lines[i*2+1].split()
    maxi=0
    for j in range(len(minions)):
        minions[j]=int(minions[j])
        maxi+=minions[j]
    for j in range(2**len(minions)):
        num=str(bin(j))
        num=num[2:]
        n=0
        for k in range(len(num)):
            if num[k]=="1":
                n+=minions[k]
        possibilities.append(n)
    for j in minions:
        possibilities.append(j)
        
    possibilities.sort()
    for j in possibilities:
        if j>=health:
            maxi-=j
            break
    print(maxi)


