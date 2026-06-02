class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        longest = left = right = 0
        

        for right in range(len(s)):
            counts[ord(s[right]) - ord('A')] += 1
            
            while (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
