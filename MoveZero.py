'''
给定一个数组nums，写一个函数将所有0移动到最后，同时保持非零元素的相对顺序。
例如，给定nums = [0, 1, 0, 3, 12]，在调用函数后，nums应该是[1, 3, 12, 0, 0]
'''

'''
个人思路：计算出 列表的总长度-零的数目=实际非零元素的个数
			在进行切片时候，可将其多余部分切掉，然后将零的数目append至末尾
'''

class MoveZero:
	def movezero(num):
		print("输入的列表为:",num)
		s = len(num)
		x = num.count(0)
		print('零的数目是:',x)
		index = 0
		for i in range(len(num)):
			if num[i]!=0:
				num[index] = num[i]
				index += 1
		num = num[:s-x]
		for m in range(x):
			num.append(0)
		return num
	if __name__ == '__main__':
		nums = [0,1,0,3,12,0,4,7]
		print(movezero(nums))
