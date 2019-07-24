class Solution:
	def isValid(self, s):
		brackets = ['()', '[]', '{}'] 
		while any(x in s for x in brackets): 
			for br in brackets: 
				s = s.replace(br, '')
		return not s


s0 = "{[]{()}}"
print(Solution().isValid(s0))

s1 = "()(){(())" 
print(Solution().isValid(s1)) 

s2 = ""
print(Solution().isValid(s2)) 

s3 = "([{}])()"
print(Solution().isValid(s3)) 


