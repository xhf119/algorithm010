def isanagram(self,s:str,t:Str)->bool:
	result =True
	tmp = set(s)
	if tmp == set(t):
		for i in tmp:
			result = result and (s.count(i) == t.count(i))
	else:
		result = False
	return (result)

���������Ƿ���ȣ��Լ����е��ַ�������һ������ȷ