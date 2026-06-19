function two_sum_ii(nums, target):
	l <- 0
	r <- len(nums) - 1
	while l < r:
		current <- nums[l] + nums[r]
		if current = target:
			return [l + 1, r + 1]
		if current < target:
			l <- l + 1
		if current > target:
			r <- r - 1
