# my O(m*logn) solution because the "in" function is a linear pass taking O(n) time :)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1

        while l<=r:
            mid = (l+r)//2
            if target in matrix[mid]:
                return True
            elif target< matrix[mid][0]:
                r=mid-1
            elif target > matrix[mid][-1]:
                l=mid+1
            else:
                return False
        return False