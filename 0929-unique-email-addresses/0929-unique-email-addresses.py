class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = {}
        for email in emails:
            a, b = email.split('@')
            c = ""
            for char in a:
                if char == '+':
                    break
                elif char != '.':
                    c += char
            uniqueEmails[c + '@' + b] = 0

        return len(uniqueEmails)








