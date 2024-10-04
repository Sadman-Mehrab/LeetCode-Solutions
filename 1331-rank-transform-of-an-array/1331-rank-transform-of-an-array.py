from collections import defaultdict
from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(arr, reverse = False)
        indexMap = defaultdict(int)
        ans = []
        idx = 1

        for s in sortedArr:
            if s not in indexMap:
                indexMap[s] = idx
                idx += 1

        for a in arr:
            ans.append(indexMap[a])

        return ans
