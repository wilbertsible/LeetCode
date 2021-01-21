class Solution:
	def divide(self, dividend:int, divisor:int)->int:
		negDivisor = 0
		negDividend = 0
		isNegativeDividend = False
		isNegativeDivisor = False
		print("to 1")
		if dividend < 0:
			print("to 2")
			isNegativeDividend = True
			while dividend != 0:
				dividend += 1
				negDividend += 1
				print(negDividend)
			dividend = dividend  + negDividend
		if divisor < 0:
			print("to 3")
			isNegativeDivisor = True
			while divisor != 0:
				divisor += 1
				negDivisor += 1
			divisor = divisor  + negDivisor
		quotient = 0
		while dividend >= divisor:
			dividend  = dividend - divisor
			quotient+=1
		posCount = 0
		if (isNegativeDividend and not isNegativeDivisor) or (isNegativeDivisor and not isNegativeDividend):
			while quotient != 0:
				quotient -=1
				posCount+=1
			for i in range(0, posCount):
				quotient -=1
			return quotient
		else:
			return quotient


s = Solution()
print(s.divide(-2147483648,-1))