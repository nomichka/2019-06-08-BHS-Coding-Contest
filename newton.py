#READING
import os
import math
path="newton.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

for i in range(N):
    lines[i]=lines[i].split()
    for j in range(len(lines[i])):
        lines[i][j]=int(lines[i][j])
    p=float(lines[i][0])
    q=float(lines[i][1])
    r=float(lines[i][2])
    s=float(lines[i][3])
    t=float(lines[i][4])
    u=float(lines[i][5])
    if p==0 and q==0 and r==0 and s==0 and t==0 and u==0:
        print("0.0000")
    else:
        close=[]
        for j in range(100000):
            x=j/100000.0
            num=p*math.exp(-x)+q*math.sin(x)+r*math.cos(x)+s*math.tan(x)+t*x*x+u
            if num<0.01 and num>-0.01: #CHANGE
                close.append([x, num])
        if len(close)==0:
            print("No solution")
        else:
            a=""
            for j in range(1, len(close)-1):
                if close[j][1]>close[j+1][1] and close[j][1]>0 and close[j+1][1]<0:
                    b=str(close[j][0])
                    if int(b[len(b)-1])<5:
                        b=str(close[j][0])[0:6]
                    else:
                        b=str(float(str(close[j][0])[0:6])+0.0001)
                    a+=b+" "
            print(a)
