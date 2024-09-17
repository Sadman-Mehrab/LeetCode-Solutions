from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        freq = defaultdict(int)
        for s in s1.split(" "):
            freq[s] += 1
        for s in s2.split(" "):
            freq[s] += 1
        for f in freq:
            if freq[f]== 1:
                ans.append(f)
        return ans
            