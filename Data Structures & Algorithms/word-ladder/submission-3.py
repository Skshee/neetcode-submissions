class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        visit = set()
        queue = deque()
        res = 1

        visit.add(beginWord)
        queue.append(beginWord)

        patternDic = defaultdict(list)
        wordList.append(beginWord) # Beginword is not in list and we need to uska patterns also

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                patternDic[pattern].append(word)
        
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in patternDic[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
                    patternDic[pattern] = []
            res += 1
        return 0