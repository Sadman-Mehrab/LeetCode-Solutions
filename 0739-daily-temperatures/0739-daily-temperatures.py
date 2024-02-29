class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while len(st) != 0 and st[-1][0] < temperatures[i]:
                idx = st.pop()[1]
                res[idx] = i - idx
            st.append([temperatures[i], i])
        
        return res