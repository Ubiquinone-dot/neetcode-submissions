class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        idxs = []
        vals = []
        
        for i in range(len(numbers)):
            

            for j in range(len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
            
        return idxs