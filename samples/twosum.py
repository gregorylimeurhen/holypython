class TwoSum:
	def __init__(self, nums, target):
		self.nums = nums
		self.target = target

	def search(self):
		l = 0
		r = len(self.nums) - 1
		while l < r:
			current = self.nums[l] + self.nums[r]
			if current == self.target:
				return [l, r]
			elif current < self.target:
				l = l + 1
			else:
				r = r - 1

nums = list(range(1, 20 + 1))
target = 25
searcher = TwoSum(nums, target)
solution = searcher.search()
print(solution)
