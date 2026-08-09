class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = {}
        bestLen = float('inf')
        bestIndex = 0

        for c in t:
            needed[c] = needed.get(c, 0) + 1

        left = 0
        right = 0

        missing = len(t)

        for right in range(len(s)):
            if s[right] in needed:
                if needed[s[right]] > 0:
                    missing -= 1
                needed[s[right]] -= 1
            while missing == 0:
                if right - left + 1 < bestLen:
                    bestLen = right - left + 1
                    bestIndex = left
                if s[left] in needed:
                    needed[s[left]] += 1

                    if needed[s[left]] > 0:
                        missing += 1
                left += 1
        
        return "" if bestLen == float('inf') else s[bestIndex:bestIndex + bestLen]

