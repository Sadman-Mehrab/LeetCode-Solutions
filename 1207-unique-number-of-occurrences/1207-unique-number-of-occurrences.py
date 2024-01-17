class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        freqSet = set()
        for n in arr:
            freq[n] += 1
        for k in freq:
            if freq[k] in freqSet:
                return False
            else:
                freqSet.add(freq[k])
        return True



