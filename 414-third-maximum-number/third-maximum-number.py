class Solution:
    def thirdMax(self, nums: List[int]) -> int:
            first_max = second_max = third_max = None

            for num in nums:
                if num == first_max or num == second_max or num == third_max:
                    continue
                    
                if first_max is None or num > first_max:
                    third_max = second_max
                    second_max = first_max
                    first_max = num
                elif second_max is None or num > second_max:
                    third_max = second_max
                    second_max = num
                elif third_max is None or num > third_max:
                    third_max = num

            if third_max is not None:
                return third_max
            else:
                return first_max
