class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Storing last seen index of characters and jumpong to them directly
        # optimized sliding window version (using a hashmap) — it avoids    removing characters one by one and instead jumps the left pointer directly.
        charIndex = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] in charIndex and charIndex[s[right]] >= left:
                left = charIndex[s[right]] + 1
            charIndex[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest

        