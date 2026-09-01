class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        res = []
        for string in strs:
            sorted_string = ''.join(sorted(string))
            dic[sorted_string].append(string)

        for val in dic.values():
            res.append(val)

        return res
        