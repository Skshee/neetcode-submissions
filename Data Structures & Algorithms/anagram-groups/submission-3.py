class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)
        res = []

        for s in strs:
            sorted_str = ''.join(sorted(s))
            print(sorted_str)
            grps[sorted_str].append(s)

        return list(grps.values())
        