class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        ans = []

        for i in range(len(strs)):
            sorted_string = ''.join(sorted(strs[i]))
            if sorted_string not in dic:
                dic[sorted_string] = [strs[i]]
            else:
                dic[sorted_string].append(strs[i])
        
        for values in dic.values():
            ans.append(values)
        
        return ans

        