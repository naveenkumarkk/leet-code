class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bucket = set()
        for i in nums:
            if i in bucket:
                return True
            bucket.add(i)
        return False
        