class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        snums = sorted(nums)
        i = 0
        for i in range(0, len(snums) - 2,1):
            if i > 0 and snums[i] == snums [i - 1]:
                continue
            l = i + 1 
            r = len(nums) - 1
            while l < r:
                target = snums[i] + snums[l] + snums[r]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    result.append([snums[i],snums[l],snums[r]])
                    l += 1
                    r -= 1
                    while l < r and snums[l] == snums[l - 1]:
                        l += 1
                    while l < r and snums[r] == snums[r + 1]:
                        r -= 1

        return result
