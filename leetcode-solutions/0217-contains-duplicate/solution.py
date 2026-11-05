class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range (len(nums) - 1):
            x = nums[i]
            y = nums[i+1]

            if x == y:
                return True
                break
        
        return False
