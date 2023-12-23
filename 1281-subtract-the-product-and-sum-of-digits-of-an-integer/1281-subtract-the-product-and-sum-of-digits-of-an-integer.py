class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        for c in str(n):
            prod *= int(c)
            summ += int(c)
        return prod - summ