class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dic1[s[i]] += 1
            dic2[t[i]] += 1

        if dic1 == dic2:
            return True
        else:
            return False
        