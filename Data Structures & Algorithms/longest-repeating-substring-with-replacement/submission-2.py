class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = right = 0
        maxLength = 0

        for right in range(len(s)):
            counts[ord(s[right]) - ord('A')] += 1

            if (right - left + 1) - max(counts) > k:
                counts[ord(s[left]) - ord('A')] -=1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
        