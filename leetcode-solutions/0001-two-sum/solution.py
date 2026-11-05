class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count1 = {}
        output = []
        for i in range(len(nums)):
            count1[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]
            if y in count1 and count1[y] != i:
                output.append(i)
                output.append(count1[y])
                return output
