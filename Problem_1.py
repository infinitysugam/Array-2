# We modify the same input array index value to negative if the values are in the array
# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(0,len(nums)):
            number = nums[i]
            index = abs(nums[i])-1

            if nums[index]>0:
                nums[index] = -nums[index]
        for i in range(0,len(nums)):
            if nums[i]>0:
                result.append(i+1)
        return result