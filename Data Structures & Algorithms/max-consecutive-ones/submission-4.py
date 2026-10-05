class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxim = 0
        current = 0
        for i in range(len(nums)):
            if nums [i] == 1:
                current +=1
                if maxim < current:
                    maxim = current
            else:
                current = 0
        return maxim 