'''
给定n表示每个条的宽度为1的高程图的非负整数，计算下雨后能够捕获的水量。
例如，给定[0,1,0,2,1,0,1,3,2,1,2,1]，返回6。
(画图可以看出来)
'''

'''
分析

对于每个柱子，找到其左右两边最高的柱子，该柱子能容纳的面积就是min(max_left, max_right) - height。
所以，
一
从左往右扫描一遍，对于每个柱子，求取左边最大值;
从右往左扫描一遍，对于每个柱子，求最大右值;
再扫描一遍，把每个柱子的面积并累加。
也可以，
二
扫描一遍，找到最高的柱子，这个柱子将数组分为两半;
处理左边一半;
处理右边一半。

'''
class Water():
	def water(A):
		n = len(A)
		The_max = 0
		for i in range(n):
			if A[i]>A[The_max]:
				The_max = i
		
		waters = 0
		left = 0
		for x in range(The_max):
			if A[x]> left:
				left = A[x]
			else:
				waters = waters+left-A[x]
		right = 0
		for s in range(n-1,The_max,-1):
			print(s)
			if A[s]>right:
				right =A[s]
			else:
				waters = waters+right-A[s]
		print(waters)
		return waters		
	if __name__=='__main__':
		A=[0,1,0,2,1,0,1,3,2,1,2,1]
		print(water(A))