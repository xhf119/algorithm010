def twoSum(self,nums,target):

	n = len(nums) # 获取nums的长度
	for x in range(n): # 外层循环先取出下标0，对应着数组里的第一个数字
		for y in range(x+1,n): # 内层循环取出下标1，对应着数组里的第二个数

			if nums[x] + nums[y] == target: # 如果第一个数字+第二个数字=target

				return x,y # 上面的判断是对的话，那么就返回下标

				break # 并停止程序
				
			else: #
				continue

def twoSum(self,nums,target):

	n = len(nums) # 获取nums的长度
	for x in range(n): # 外层循环
		a = target -nums[x]
		if a in nums:
			y =nums.index(a)
			if x == y:
				continue
			else:
				return x,y
 
				break # 并停止程序
				
			else: #
				continue
				break
		else:
			continue


把数组里的数字作为key，下标作为value存到d字典中
def twoSum(self,nums,target):

	d = {}

	n = len(nums)
	for x in range(n):

		if target - nums[x] in d:

			return d[target-nums[x]],x

		else:

			d[nums[x]] = x

