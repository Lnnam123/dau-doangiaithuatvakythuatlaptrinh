class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        total_time = 0
        target_tickets = tickets[k]
        for i in range (len(tickets)):
            if i <= k:
                # Người đứng trước hoặc là k: mua tối đa bằng số vé của k
                total_time += min(tickets[i], target_tickets)
            else:
                # Người đứng sau k: mua tối đa bằng số vé của k - 1
                total_time += min(tickets[i], target_tickets - 1)
        return total_time

