filename = r'C:\Users\鹏COMPUTER\Desktop\cat.txt'
l =[]
v =[""]*len(open(filename).readlines())
with open(filename,'r') as f:
    for line in f:
        line = line.replace("\n","").split(",")
        l.append(line)
for i in range(1,4):
    v[i] = dict(zip(l[0],l[i]))

with open(r'C:\Users\鹏COMPUTER\Desktop\cat1.txt','w') as f:
    for i in range(4):
        f.write(str(v[i]) + "\n")

