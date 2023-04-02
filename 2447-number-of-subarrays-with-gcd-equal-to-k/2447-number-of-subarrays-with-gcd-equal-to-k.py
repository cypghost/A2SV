class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:  
                return a

            return gcd(b, a % b)
        
        count = 0
        
        for index in range(len(nums)):
            val = nums[index]
            
            for idx in range(index, len(nums)):
                val = gcd(val, nums[idx])
                    
                if val == k:
                    count += 1
                
                elif val < k:
                    break
                
        return count