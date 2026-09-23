class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            missing = target - nums[i]
            if missing in seen:
                if i > seen.get(missing):
                    return [seen.get(missing), i]
                return [i, seen.get(missing)]

            seen[nums[i]] = i

        return []