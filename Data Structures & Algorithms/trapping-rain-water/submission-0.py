class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        leftmax,rightmax = height[l],height[r]
        res=0
    # water stored at every index will be the "min(leftmax,rightmax) of every index " - "height[of that index]"

        while l<r:
            if leftmax<rightmax:
                l+=1
                leftmax=max(leftmax,height[l])
                 # water stored at every index will be the "min(leftmax,rightmax) of every index " - "height[of that index]"
                res += leftmax - height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                 # water stored at every index will be the "min(leftmax,rightmax) of every index " - "height[of that index]"
                res += rightmax - height[r]
        return res