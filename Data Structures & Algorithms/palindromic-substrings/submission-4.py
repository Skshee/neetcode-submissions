class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.count = 0

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                self.count += 1
                left -= 1
                right += 1

        for i in range(n):
            # Odd-length palindromes
            expand(i, i)

            # Even-length palindromes
            expand(i, i + 1)

        return self.count