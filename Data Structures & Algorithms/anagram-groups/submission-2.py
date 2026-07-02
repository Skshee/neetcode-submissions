class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = ''.join(sorted(s))


            dic[sorted_s].append(s)
        
        for val in dic.values():
            res.append(val)
        return res
