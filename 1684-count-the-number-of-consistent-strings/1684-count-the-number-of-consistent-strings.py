class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        count = 0
        
        for w in words:
            flag = True
            for c in w:
                if c not in allowedSet:
                    flag = False
                    break
            if flag:
                count += 1
                
        return count