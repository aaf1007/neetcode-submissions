class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r and numbers[l] + numbers[r] - target != 0:
            diff = numbers[l] + numbers[r] - target
            
            if l < r and diff > 0:
                r -= 1

            if l < r and diff < 0:
                l += 1

        return [l+1, r+1]
