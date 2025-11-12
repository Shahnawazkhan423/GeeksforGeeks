class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        remove  = set(arr)
        second_largest = 0
        large = max(remove)
        for i in remove:
            if second_largest<i and i!=large:
                second_largest=i  
        if second_largest==0:
            return  -1 
        else:
            return second_largest