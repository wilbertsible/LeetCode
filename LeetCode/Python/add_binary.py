class Solution:
    def add_binary(self, a:str, b:str)->str:
        return str(bin(int(a,2) + int(b,2))[2:])

s = Solution()

a = "100"
b = "1"
print(s.add_binary(a, b))
