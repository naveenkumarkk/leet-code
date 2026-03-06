class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucket = [[] for _ in range(len(nums)+1)]
        ans = []
        maxElement = 0
        for n in nums:
            if n in hashMap:
                hashMap[n] = hashMap[n] + 1
                if hashMap[n] > maxElement:
                    maxElement = hashMap[n]
            else:
                hashMap[n] = 1
        
        for key,value in hashMap.items():
            bucket[value].append(key)
        count = 0
        
        for i in range(len(nums),-1,-1):
            for val in bucket[i]:
                if val != '':
                    ans.append(val)
                    count += 1
                if count == k:
                    return ans
        return ans