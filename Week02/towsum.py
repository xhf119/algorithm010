def twoSum(self,nums,target):

	n = len(nums) # ��ȡnums�ĳ���
	for x in range(n): # ���ѭ����ȡ���±�0����Ӧ��������ĵ�һ������
		for y in range(x+1,n): # �ڲ�ѭ��ȡ���±�1����Ӧ��������ĵڶ�����

			if nums[x] + nums[y] == target: # �����һ������+�ڶ�������=target

				return x,y # ������ж��ǶԵĻ�����ô�ͷ����±�

				break # ��ֹͣ����
				
			else: #
				continue

def twoSum(self,nums,target):

	n = len(nums) # ��ȡnums�ĳ���
	for x in range(n): # ���ѭ��
		a = target -nums[x]
		if a in nums:
			y =nums.index(a)
			if x == y:
				continue
			else:
				return x,y
 
				break # ��ֹͣ����
				
			else: #
				continue
				break
		else:
			continue


���������������Ϊkey���±���Ϊvalue�浽d�ֵ���
def twoSum(self,nums,target):

	d = {}

	n = len(nums)
	for x in range(n):

		if target - nums[x] in d:

			return d[target-nums[x]],x

		else:

			d[nums[x]] = x

