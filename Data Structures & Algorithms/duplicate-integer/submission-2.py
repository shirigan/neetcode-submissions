class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set()
        for i in nums:
            if i not in new:
                new.add(i)
            else:
                 return True
        return False
        