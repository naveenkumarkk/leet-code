class Solution:
    def candy(self, ratings: List[int]) -> int:
        shadown_list = [1] * (len(ratings))
        
        for i in range(len(ratings)-1):
            if ratings[i] < ratings[i+1]:
                shadown_list[i+1]=shadown_list[i]+1

        print(shadown_list)
        for i in range(len(ratings)-2,-1,-1):
           if ratings[i] > ratings[i+1] :
                shadown_list[i] = max(shadown_list[i], shadown_list[i + 1] + 1)
        print(shadown_list)
    
        return sum(shadown_list)