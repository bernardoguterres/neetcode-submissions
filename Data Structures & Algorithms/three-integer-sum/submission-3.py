class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        snums = sorted(nums)
        result = []
        i = 0
        for i in range (0,len(snums) - 2,+1):
            if i > 0 and snums[i] == snums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if snums[i] + snums[l] + snums[r] > 0:
                    r -= 1
                elif snums[i] + snums[l] + snums[r] < 0:
                    l += 1
                else:
                    result.append([snums[i], snums[l], snums[r]])
                    l += 1
                    while snums[l] == snums[l - 1] and l < r:
                        l += 1

        return result


