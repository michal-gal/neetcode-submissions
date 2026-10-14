class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_equal = 0
        lenght = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] != val:
                not_equal += 1
                i += 1
            else:
                nums.pop(i)
        return not_equal

        