class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_prod = None
        # init arr to be all 1
        ans = [1] * len(nums)

        # l to r pass
        for i in range(len(nums)):
            if running_prod == None:
                running_prod = nums[i]
                continue

            ans[i] *= running_prod
            running_prod *= nums[i]

        running_prod = None
        i = len(nums) - 1

        # r to l pass
        while i >= 0:
            if running_prod == None:
                running_prod = nums[i]
                i -= 1
                continue

            ans[i] *= running_prod
            running_prod *= nums[i]
            i -= 1

        return ans
