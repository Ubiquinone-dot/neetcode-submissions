class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n-1
        while left < right:
            tot = numbers[left] + numbers[right]
            if tot==target:
                return [left+1, right+1]
            elif tot < target:
                left += 1
            elif tot > target:
                right -= 1
            # elif left >= right:
            #     return []