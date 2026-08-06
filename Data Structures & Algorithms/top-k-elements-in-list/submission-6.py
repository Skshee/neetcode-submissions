class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using Bucket Sort where basically we have a hashmap where keys is the counts/occurences and value is the number that has occured those many time
        n = len(nums)
        count = {} # Key : Num, Value : occurences
        freq = [[] for _ in range(n+1)] # Basically storing numbers to their respective occurences
        res = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, count in count.items():
            freq[count].append(num)

        for i in range(len(freq)-1, 0, -1):
            for val in freq[i]:
                res.append(val)
            if len(res) == k:
                return res

