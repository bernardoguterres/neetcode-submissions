class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1 
        for num,f in seen.items():
            freq[f].append(num)
        result = []
        for i in range(len(nums), 0, -1):
            result.extend(freq[i])
            if len(result) == k:
                return result

        