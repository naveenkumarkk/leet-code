class Solution:
    def trap(self, height: List[int]) -> int:
        
        array_len = len(height)
        max_left = [0] * array_len
        max_right = [0] * array_len
        result =[0] * array_len
        max_left_value = height[0]
        for i in range(1,array_len):
            max_left_value = max(max_left_value,height[i-1])
            max_left[i] = max_left_value
        
        max_right_value = height[array_len-1]
        
        for i in range(array_len-2,-1,-1):
            max_right_value = max(max_right_value,height[i+1])
            max_right[i] = max_right_value
        
        total = 0
        for i in range(array_len):
            water = min(max_left[i], max_right[i]) - height[i]
            total += max(water, 0)
        return total
            
        