class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in hash:
                return [hash[complement],i]
            hash[nums[i]] = i