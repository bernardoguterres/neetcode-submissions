class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        running = 1
        for i,num in enumerate(nums):
            result[i] *= running
            running *= num

        running = 1
        for i in range(len(nums) - 1,-1,-1):
            result[i] *= running
            running *= nums[i]
        return result
        