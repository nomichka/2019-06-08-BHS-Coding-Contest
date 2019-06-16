#READING
import os
path="intersect.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

for i in range(N):
    lines[i]=lines[i].split()
    indX1=lines[i][0].index("x")
    a1=int(lines[i][0][0:indX1])
    b1=int(lines[i][0][indX1+1:])
    oA1=a1
    oB1=b1
    
    indX2=lines[i][1].index("x")
    a2=int(lines[i][1][0:indX2])
    b2=int(lines[i][1][indX2+1:])

    
    if b1==b2:
        print("true")
    elif a1==a2:
        print("false")
    else:
        print("true")
 

