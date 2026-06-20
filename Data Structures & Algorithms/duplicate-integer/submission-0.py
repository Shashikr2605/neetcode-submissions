class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash=[]
        for i in range(0,len(nums)):
            if nums[i] not in hash:
                hash.append(nums[i])
            else:
                return True
        return False