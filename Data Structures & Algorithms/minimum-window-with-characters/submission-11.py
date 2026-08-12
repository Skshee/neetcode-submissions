class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needs = Counter(t)
        missing = len(t)
        counts = {}
        bestLen = float('inf')
        bestIndex = 0

        left = right = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            if s[right] in needs:
                if counts[s[right]] <= needs[s[right]]:
                    missing -= 1
            while missing == 0:
                if bestLen > right - left + 1:
                    bestLen = right - left + 1
                    bestIndex = left

                counts[s[left]] -= 1
                if s[left] in needs:
                    if counts[s[left]] < needs[s[left]]:
                        missing += 1
                left += 1
        return s[bestIndex:bestIndex + bestLen] if bestLen != float('inf') else "" 



        