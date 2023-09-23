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
            uniqueEmails[c + '@' + b] = True

        return len(uniqueEmails)








