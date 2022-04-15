class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for val in nums:
            count[val] = 1 + count.get(val, 0)
        for num, count in count.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq) - 1, 0, - 1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result