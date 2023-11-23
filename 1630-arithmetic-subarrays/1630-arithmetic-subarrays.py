class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        left = 0
        right = 0
        res = []
        
        while left < len(l) and right < len(r):
            a = sorted(nums[l[left]:r[right] + 1])
            print(a)
            for i in range(len(a) - 1, 1,-1):
                if a[i] - a[i - 1] != a[i - 1] - a[i - 2]:
                    res.append(False)
                    break
            
            else:
                res.append(True)
            
            left += 1
            right += 1
            
        return res
                
            
                