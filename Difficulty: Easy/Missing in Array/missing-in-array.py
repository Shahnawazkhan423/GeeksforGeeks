class Solution:
    def missingNum(self, arr):
        # code here
        arr_set = set(arr)
        max_val = max(arr)
        for i in range(1, max_val + 1):
            if i not in arr_set:
                return i
        return max_val + 1