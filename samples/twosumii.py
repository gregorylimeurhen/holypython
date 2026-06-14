class TwoSumII:
	def __init__(self, nums, target):
		self.nums = nums
		self.target = target

	def search(self):
		l = 0
		r = len(self.nums) - 1
		while l < r:
			current = self.nums[l] + self.nums[r]
			if current == self.target:
				return [l + 1, r + 1]
			if current < self.target:
				l = l + 1
			if current > self.target:
				r = r - 1
