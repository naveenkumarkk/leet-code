class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        target = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[i],target)
            else:
                res += min(tickets[i],target-1)

        return res


