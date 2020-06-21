def isanagram(self,s:str,t:Str)->bool:
	result =True
	tmp = set(s)
	if tmp == set(t):
		for i in tmp:
			result = result and (s.count(i) == t.count(i))
	else:
		result = False
	return (result)

两个集合是否相等，对集合中的字符计数，一样则正确