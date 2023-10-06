func maxProfit(prices []int) int {
    l := 0
	maxProfit := 0
	for r := 1 ; r < len(prices) ; r++ {
		if prices[r] > prices[l] {
			if prices[r] - prices[l] > maxProfit {
				maxProfit = prices[r] - prices[l]
			}
		} else {
			l = r
		}
	}
	return maxProfit

}