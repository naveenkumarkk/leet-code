class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = 0
        dist = math.inf
        nums.sort()
        
        for i in range(len(nums)):
            #if nums[i] gets too big, return the best result so far
            if 3*nums[i]-target >= dist:
                break
            #skip the duplicate values as it is only redundant
            #computation
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            j = i+1
            k = len(nums)-1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
            
                if total > target:
                    k -= 1
                    #we already know that total>target
                    if total-target < dist:
                        res = total
                        dist = total-target
                elif total < target:
                    j += 1
                    #we already know that target>total
                    if target-total < dist:
                        res = total
                        dist = target-total

                    #because the current j is too small, we can skip
                    #all the duplicates
                    while j < len(nums) and nums[j-1]==nums[j]:
                        j += 1
                else:
                    return target
        return res