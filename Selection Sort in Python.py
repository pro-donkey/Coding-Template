class Solution:
    def selectionSort(self, nums):
        # Get the length of the list
        n = len(nums)
        
        # Traverse through all list elements
        for i in range(0, n - 1):
            mn = i  # Assume the current index has the minimum
            
            # Find the minimum element in the unsorted portion
            for j in range(i + 1, n):
                if nums[j] < nums[mn]:
                    mn = j
            
            # Swap only if a smaller element was found
            if mn != i:
                nums[mn], nums[i] = nums[i], nums[mn]
        
        return nums  # Return the sorted list
