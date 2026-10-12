class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = []

        n = len(word1)
        m = len(word2)

        if n == m:
            for i in range(n):
                temp.append(word1[i])
                temp.append(word2[i])
        elif n < m:
            for i in range(n):
                temp.append(word1[i])
                temp.append(word2[i])
            for j in range(n, m):
                temp.append(word2[j])
        else:
            for i in range(m):
                temp.append(word1[i])
                temp.append(word2[i])
            for j in range(m,n):
                temp.append(word1[j])
        
        newString = ''.join(temp)
        return newString