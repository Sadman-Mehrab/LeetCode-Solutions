class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([1 for detail in details if int(detail[-4:-2]) > 60])