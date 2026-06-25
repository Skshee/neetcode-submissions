class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backTrack(start, curr):
            # If we've used all characters, we found one partition
            if start == len(s):
                ans.append(curr[:])
                return

            # Try every possible substring starting at 'start'
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                # Only continue if the substring is a palindrome
                if substring == substring[::-1]:
                    curr.append(substring)
                    backTrack(end + 1, curr)
                    curr.pop()

        backTrack(0, [])
        return ans