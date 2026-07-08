class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        while l<r:
            mid = (l+r)//2
            if nums[mid] < nums[r]:
                r=mid
            else:
                l = mid+1
        piv = l

        if target>= nums[piv] and target <= nums[len(nums)-1]:
            le,ri = piv, len(nums)-1
            while le<=ri:
                m=(le+ri)//2
                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    le=m+1
                else:
                    ri = m-1
        if target > nums[len(nums)-1]:
            left,right = 0, piv-1
            while left<=right:
                mi=(left+right)//2
                if target == nums[mi]:
                    return mi
                elif target > mi:
                    left=mi+1
                else:
                    right = mi-1
        return -1