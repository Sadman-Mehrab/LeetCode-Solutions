class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        emptyBottles = 0
        while emptyBottles >= numExchange or numBottles != 0:
            total += numBottles
            emptyBottles += numBottles
            numBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
        return total