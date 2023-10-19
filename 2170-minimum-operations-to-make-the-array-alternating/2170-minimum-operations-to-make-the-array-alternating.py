class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        even = sorted(Counter([val for i, val in enumerate(nums) if i % 2 == 0]).items(), key = itemgetter(1), reverse = True)

        odd = sorted(Counter([val for i, val in enumerate(nums) if i % 2]).items(), key = itemgetter(1), reverse = True)
        
        if even[0][0] != odd[0][0]:
            return len(nums) - even[0][1] - odd[0][1]

        else:
            ret = 10 ** 5 + 1
            
            if len(even) == len(odd) == 1:
                return odd[0][1]

            if len(even) > 1:
                ret = min(ret, len(nums) - even[1][1] - odd[0][1])

            if len(odd) > 1:
                ret = min(ret, len(nums) - even[0][1] - odd[1][1])

            return ret 

        return 0