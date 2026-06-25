class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        mappings = {
            '2' : 'abc', '3' : 'def', '4' : 'ghi', '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'
        }

        ans = []

        def backTrack(i, curr):
            if i == len(digits):
                ans.append("".join(curr))
                return

            for letter in mappings[digits[i]]:
                curr.append(letter)
                backTrack(i+1, curr)
                curr.pop()
        backTrack(0, [])
        return ans