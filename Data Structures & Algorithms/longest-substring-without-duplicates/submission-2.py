class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        res = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.append(s[right])
            res = max(res, right - left + 1)
        
        return res

