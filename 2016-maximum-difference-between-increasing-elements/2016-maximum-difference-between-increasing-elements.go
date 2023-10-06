func maximumDifference(nums []int) int {
    i := 0
	maxDifference := -1
	for j := 1 ; j < len(nums) ; j++ {
		if nums[j] > nums[i] {
			if nums[j] - nums[i] > maxDifference {
				maxDifference = nums[j] - nums[i]
			}
		} else {
			i = j
		}
	}
	return maxDifference
}