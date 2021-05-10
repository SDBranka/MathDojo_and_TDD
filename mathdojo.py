# Create a Python class called MathDojo that has one attribute, result, and 2 methods: add and subtract. The 2 methods each must take at least 1 parameter, but could take many more.
class MathDojo:
    def __init__(self):
    	self.result = 0
    
    def add(self, num, *nums):
    	# your code here
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
    	# your code here
        self.result -= num
        for n in nums:
            self.result -= n
        return self
