from collections import defaultdict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result = []
        stringMap = defaultdict(int)
        
        for a in arr:
            stringMap[a] += 1
        
        for key in arr:
            if stringMap[key] == 1:
                result.append(key)
        
        
        if k > len(result):
            return ""
        else:
            return result[k-1]