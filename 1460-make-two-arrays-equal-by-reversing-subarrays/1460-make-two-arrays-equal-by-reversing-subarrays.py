from collections import defaultdict
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq = defaultdict(int)
        
        for t in target:
            freq[t] += 1
        
        for a in arr:
            freq[a] -= 1
            
        for k in freq:
            if freq[k] != 0:
                return False
        
        return True
        
    