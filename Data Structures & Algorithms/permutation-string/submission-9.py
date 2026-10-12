class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1) # S1 - abc
        m = len(s2) # S2 - lecabee
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        if n > m:
            return False

        for char in s1:
            s1_counts[ord(char)-ord('a')] += 1
        
        for i in range(n):
            s2_counts[ord(s2[i]) - ord('a')] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(n, m):
            s2_counts[ord(s2[i-n]) - ord('a')] -= 1
            s2_counts[ord(s2[i]) - ord('a')] += 1

            if s1_counts == s2_counts:
                return True
        return False