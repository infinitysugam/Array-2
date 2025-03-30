# Time complexity = O(n)
# Space Complexity = O(1)
class Solution:
    def get_min_max(self, arr):
        minimum = float('inf')
        maximum = -float("inf")
        
        size = len(arr)
        flag = False
        if size%2!=0:
            flag = True
            size = size -1 
            
        for i in range(0,size,2):
            if arr[i]<=arr[i+1]:
                minimum = min(arr[i],minimum)
                maximum = max(arr[i+1],maximum)
            else:
                maximum = max(arr[i],maximum)
                minimum = min(arr[i+1],minimum)
        
        if flag:
            if arr[-1] >= maximum:
                maximum = arr[-1]
            
            if arr[-1] <= minimum:
                minimum = arr[-1]
        
        
        return minimum,maximum
                