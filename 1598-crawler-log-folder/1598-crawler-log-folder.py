class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "../" and ans == 0:
                continue
            elif log == "../":
                ans -= 1
            elif log == "./":
                continue
            else:
                ans += 1
        return ans