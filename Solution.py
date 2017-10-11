'''
给定一个排序的数组，删除重复的位置，使每个元素只显示一次并返回新的长度。+

不要为另一个数组分配额外的空间，您必须使用常量内存来执行此操作。
例如，给定输入数组A = [1,1,2]，
你的函数应该返回length = 2，A现在是[1,2]。
'''
class Solution:
	def Solute(num):
		if num=='':
			return 
		index = 1
		for i in range(len(num)):
			if num[i] != num[index-1]:
				num[index] = num[i]
				index +=1
		return index
	if __name__ == '__main__':
		a = [1,1,2,2,2,3,3,4]
		print(Solute(a))

'''
for循环中的递增迭代： for i in range(len(numbers)): 对于数组的索引迭代，
	需要用到len（）求数组的长度，用range进行索引迭代。
'''
