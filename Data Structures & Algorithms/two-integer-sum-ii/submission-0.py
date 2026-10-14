class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            
            if l < r and target - total < 0:
                r -= 1
                continue

            if l < r and target - total > 0:
                l += 1
                continue
            
            break

        return [l+1, r+1]
