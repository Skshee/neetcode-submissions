class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        print(need)
        formed = 0
        required = len(need)
        print(required)
        left = right = 0
        minLen = float('inf')
        subStr = [-1, -1]
        counts = {}

        for right in range(len(s)):
            if s[right] not in counts:
                counts[s[right]] = 1
            else:
                counts[s[right]] += 1

            if s[right] in need:
                if counts[s[right]] == need[s[right]]:
                    formed += 1
            
            while formed == required:
                if (right - left + 1) < minLen:
                    minLen = right - left + 1
                    subStr = [left, right]

                counts[s[left]] -= 1
                if s[left] in need and counts[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1
        return s[subStr[0]:subStr[1]+1]
            

