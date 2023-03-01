class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        
        for num in nums:
            prefix.append(prefix[-1] + num)

        ans = len(nums) + 1 
        m_queue = collections.deque() 
            
        for num, val in enumerate(prefix):
            
            
            while m_queue and val <= prefix[m_queue[-1]]:
                m_queue.pop()
                
            while m_queue and val - prefix[m_queue[0]] >= k:
                ans = min(ans, num - m_queue.popleft())

            m_queue.append(num)

        return ans if ans < len(nums) + 1 else -1