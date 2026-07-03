class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [] # pair of (index,height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: #keeps popping from the stack untill the topmost element of the stack is greater than the current element !
                index, height = stack.pop()
                maxarea = max(maxarea, height*(i-index))
                start = index
            stack.append((start,h))

        for i,h in stack:
            maxarea = max(maxarea, h*(len(heights)-i))
        return maxarea