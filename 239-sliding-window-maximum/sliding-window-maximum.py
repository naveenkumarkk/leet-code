class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dq = collections.deque()

        left = right = 0

        while right < len(nums):

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            if left > dq[0]:
                dq.popleft()
            
            if right + 1 >= k:
                output.append(nums[dq[0]])
                left += 1
            right += 1
        return output
