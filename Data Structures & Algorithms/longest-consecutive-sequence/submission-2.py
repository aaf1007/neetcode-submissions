class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            [0,3,2,5,4,6,1,1]
             ^
            curr = 1
            count = 2
            
            turn arr into a set
            {0,3,2,5,4,6,1}
        """

        nums_set = set(nums)

        ans = 0

        for num in nums_set:
            count = 1
            hasNext = True
            curr = num

            if curr - 1 in nums_set:
                continue
                
            while hasNext:
                if curr + 1 in nums_set:
                    curr += 1
                    count += 1
                    continue
                hasNext = False
            
            ans = max(ans, count)
            count = 1

        return ans