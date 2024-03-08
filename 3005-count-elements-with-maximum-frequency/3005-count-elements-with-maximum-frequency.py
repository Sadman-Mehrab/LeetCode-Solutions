class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        maxFreq = 0
        freqEls = 0
        for n in nums:
            freq[n] += 1
        for k in freq:
            if freq[k] > maxFreq:
                maxFreq = freq[k]
        for k in freq:
            if freq[k] == maxFreq:
                freqEls += 1
        return (freqEls * maxFreq)