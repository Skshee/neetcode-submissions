class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Storing last seen index of characters and jumping to them directly
        # optimized sliding window version (using a hashmap) — it avoids    removing characters one by one and instead jumps the left pointer directly.
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
        