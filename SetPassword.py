import random
import string
def mima(digt):
	m = ''
	for i in range(digt):
		m += random.choice(string.digits+string.hexdigits)
	return m

def calcu():
	number = []
	i =1
	for i in range(200):
		number.append('第'+str(i)+'个密码是:'+mima(6)+'\n')
	x = ''.join(number)
	return x

f = open(r'D:\x.txt','w')
f.write(calcu())
f.close()