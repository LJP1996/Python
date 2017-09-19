def Counts(n,m):
	print(n)
	if(n>5000):
		return Cmds(n/2,m)
	else:
		return Counts(n*2,m)

def Cmds(n,m):
	print(int(n))
	if(n/2>0):
		if(n==m):
			return 0
		return Cmds(n/2,m)

def C():
	x = int(input('请输入您需要计算的数:'))
	Counts(x,x)
	
C()