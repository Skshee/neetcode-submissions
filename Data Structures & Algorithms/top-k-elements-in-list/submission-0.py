class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        ans = []

        for num in nums:
            dic[num] += 1

        sorted_dic = sorted(dic.items(), key = lambda item : item[1], reverse = True)
        
        for num, freq in sorted_dic:
            if k > 0:
                ans.append(num)
                k -= 1
            else:
                break
        
        return ans