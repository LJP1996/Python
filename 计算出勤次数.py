import re

f = open(r'D:/p.txt','r')
f_list = f.readlines()
m= ''.join(f_list)
ba = re.compile(r'[\u4e00-\u9fa5]+')
n = ba.findall(m)
for i in set(n):
	print(i,n.count(i))