# approach: similar to counting / bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {} #frequency of numbers
        freqArr = [[] for i in range(len(nums) + 1)] #for every count(frequency), assign an empty array(numbers corresponding to that count will be pushed to the arrays)
        # assign number freqs to map
        for i in nums:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1
        # assign numbers corresponding to frequency to frequency array
        for key in freqMap:
            freqArr[freqMap[key]].append(key)

        #array for returning results
        ret = []
        #traverse frequency array in reverse (since top k elements are wanted) and push most frequent numbers to results array
        for i in range(len(freqArr)-1, 0, -1):
            for n in freqArr[i]:
                ret.append(n)
                if len(ret) == k: #return if k is satisfied 
                    return ret
        