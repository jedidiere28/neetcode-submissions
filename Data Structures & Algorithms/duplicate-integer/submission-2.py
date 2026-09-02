class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(numSet) - len(nums) == 0:
            return False
        else:
            return True