class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}

        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        reqd_counts = t_counts.copy()

        reqd = len(t)

        left = right = 0

        bestLen = float('inf')
        bestStart = 0

        while right < len(s):

            # Expand window
            if s[right] in t_counts:
                if reqd_counts[s[right]] > 0:
                    reqd -= 1

                reqd_counts[s[right]] -= 1

            # Shrink window
            while reqd == 0:
                currLen = right - left + 1

                if currLen < bestLen:
                    bestLen = currLen
                    bestStart = left

                if s[left] in t_counts:
                    reqd_counts[s[left]] += 1

                    if reqd_counts[s[left]] > 0:
                        reqd += 1

                left += 1

            right += 1

        if bestLen == float('inf'):
            return ""

        return s[bestStart:bestStart + bestLen]