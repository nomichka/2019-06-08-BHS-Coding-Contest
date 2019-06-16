#READING
import os
path="contractions.txt"
fin=open(os.path.join("D:\\JudgeFiles\\", path), "r")
#fin = open(path, "r")
lines=fin.readlines()
N=int(lines[0])
lines.remove(lines[0])

for i in range(N):
    while "n.t" in lines[i]:
        ind=lines[i].index("n.t")
        lines[i]=lines[i][0:ind]+" not" + lines[i][ind+3:]
    while ".ll" in lines[i]:
        ind=lines[i].index(".ll")
        if lines[i][ind+1:ind+3]=="ll":
            lines[i]=lines[i][0:ind]+" will" + lines[i][ind+3:]
    while ".re" in lines[i]:
        ind=lines[i].index(".re")
        lines[i]=lines[i][0:ind]+" are" + lines[i][ind+3:]
    while '.ve' in lines[i]:
        ind=lines[i].index(".ve")
        lines[i]=lines[i][0:ind]+" have" + lines[i][ind+3:]
    print(lines[i])



