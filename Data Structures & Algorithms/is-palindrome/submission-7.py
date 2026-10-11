class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        
        newStr = ''.join(chars)
        return newStr == newStr[::-1]


        