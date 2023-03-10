class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0] * k
        minUnfairness = float('inf')
        
        def backtrack(bucket, start):
            nonlocal minUnfairness
            
            if start >= len(cookies):
                minUnfairness = min(minUnfairness, max(bucket))
                return 
            
            if max(bucket) >= minUnfairness:
                return

            for index in range(k):
                bucket[index] += cookies[start]
                backtrack(bucket, start + 1)
                bucket[index] -= cookies[start]

        cookies.sort(reverse=True)      
        backtrack(bucket, 0)
        
        return minUnfairness

