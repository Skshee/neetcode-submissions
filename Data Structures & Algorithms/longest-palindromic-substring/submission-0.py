class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            # left and right are one step outside the palindrome
            return left + 1, right - 1

        ans = [0, 0]

        for i in range(n):
            # Odd-length palindrome
            l, r = expand(i, i)
            if r - l > ans[1] - ans[0]:
                ans = [l, r]

            # Even-length palindrome
            l, r = expand(i, i + 1)
            if r - l > ans[1] - ans[0]:
                ans = [l, r]

        return s[ans[0]:ans[1] + 1]