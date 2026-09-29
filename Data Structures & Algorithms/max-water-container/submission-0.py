class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
            area: h x w
            [1,7,2,5,4,7,3,6]
               ^       ^

            curr = min(7,7) x abs(1-6) = 3 x 5

            max = 36

            if same the move l
            move ptr that is smaller
        """

        l, r = 0, len(heights) - 1
        ans = 0
        curr = 0

        while l < r:
            curr = min(heights[l], heights[r]) * abs(l - r)

            ans = max(curr, ans)

            if heights[l] < heights[r]:
                l += 1
                continue

            r -= 1

        return ans