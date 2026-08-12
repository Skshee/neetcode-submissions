class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window = len(s1)
        reqd = [0 for _ in range(26)]
        curr = [0 for _ in range(26)]
        left = 0

        for c in s1:
            reqd[ord(c) - ord('a')] += 1

        for i in range(window):
            curr[ord(s2[i]) - ord('a')] += 1

        if curr == reqd:
            return True

        for right in range(window, len(s2)):
            curr[ord(s2[left]) - ord('a')] -= 1
            curr[ord(s2[right]) - ord('a')] += 1
            if curr == reqd:
                return True
            left += 1
        return False

        
