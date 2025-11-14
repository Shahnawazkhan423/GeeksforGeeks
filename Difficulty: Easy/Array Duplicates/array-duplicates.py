class Solution:
    def findDuplicates(self, arr):
        # code here 
        seen = set()
        dup = set()
        for num in arr:
            if num in seen:
                dup.add(num)
            else:
                seen.add(num)
        return list(dup)
                