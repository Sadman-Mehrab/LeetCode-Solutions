class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = {}
        words = s.split(" ")

        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in mp:
                mp[pattern[i]] = words[i]
            else:
                if mp[pattern[i]] != words[i]:
                    return False
        
        mp = {}

        for i in range(len(pattern)):
            if words[i] not in mp:
                mp[words[i]] = pattern[i]
            else:
                if mp[words[i]] != pattern[i]:
                    return False
                
        return True
    

