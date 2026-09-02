class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm_s1 = [0] * 26
        perm_s2 = [0] * 26
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        for char in s1:
            perm_s1[ord(char) - ord('a')] += 1
        
        for i in range(n):
            perm_s2[ord(s2[i]) - ord('a')] += 1
        
        if perm_s1 == perm_s2:
            return True

        for i in range(n, m):
            perm_s2[ord(s2[i]) - ord('a')] += 1
            perm_s2[ord(s2[i-n]) - ord('a')] -= 1

            if perm_s1 == perm_s2:
                return True
        return False