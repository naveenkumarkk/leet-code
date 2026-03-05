class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        heap = []
        for num, freq in freqs.items():
            if len(heap) < k:
                heappush(heap, (freq, num))
            elif heap[0][0] < freq:
                heappushpop(heap, (freq, num))
        
        return [num for _, num in heap]