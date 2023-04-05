class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        all_xor = 0
        count = 0

        for num in nums:
            all_xor |= num 

        for index in range(2 ** len(nums)):
            ans = []

            for idx in range(index.bit_length()):
                if 1 & index >> idx == 1:
                    ans.append(nums[idx])
                
            res.append(ans)
            xor = 0
            
            for idx in range(len(ans)):
                xor |= ans[idx]

            if xor == all_xor:
                count += 1
        
        return count
            


