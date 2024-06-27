class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = defaultdict(int)
        ans = 0
        n = len(edges)
        for e in edges:
            freq[e[0]] += 1
            freq[e[1]] += 1
        for k in freq:
            if freq[k] == n:
                ans = k
        return ans
            
        