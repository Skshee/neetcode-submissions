class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ans = []

        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        
        sorted_dict_desc = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        
        for num, freq in sorted_dict_desc.items():
            if k > 0:
                ans.append(num)
                k -= 1
            else:
                break
        return ans