class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        ans = set()
    
        def primefactorization(num, ans):
            if num == len(nums):
                return len(ans)
            
            prime = 2
        
            while prime * prime <= nums[num]:
                while nums[num] % prime == 0:
                    ans.add(prime)
                    nums[num] //= prime
                
                prime += 1
                
            if nums[num] > 1:
                ans.add(nums[num])
            
            primefactorization(num + 1, ans)
            
            return len(ans)
        
        return primefactorization(0, ans)
                
            


        
