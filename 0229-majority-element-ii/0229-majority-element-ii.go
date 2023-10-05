func majorityElement(nums []int) []int {
    c1, c2, f1, f2 := 0, 0, 0, 0
	for i := 0 ; i < len(nums) ; i++ {
		if f1 == 0 && nums[i] != c2{
			c1 = nums[i]
			f1 = 1
		} else if f2 == 0 && nums[i] != c1 {
			c2 = nums[i]
			f2 = 1
		} else if nums[i] == c1 {
			f1++
		} else if nums[i] == c2 {
			f2++
		} else {
			f1--
			f2--
		}
	}
	f1, f2 = 0, 0
	for i := 0 ; i < len(nums) ; i++ {
		if nums[i] == c1{
			f1++
		} else if nums[i] == c2 {
			f2++
		}
	}
	ret := []int{}
	n := len(nums)

	if f1 > n/3 {
		ret = append(ret, c1)
	}
	if f2 > n/3 {
		ret = append(ret, c2)
	}

	return ret
	
}