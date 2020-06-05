class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tempSet = set(nums)

        for i in range(len(nums)+1):
            if i not in tempSet:
                return i