class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = 1
        
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                current = num
                length = 1
                while current + 1 in seen:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest
        