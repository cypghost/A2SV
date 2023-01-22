class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstr = sorted([str(num) for num in nums])
        curr = [numstr[0]]
        
        for index in range(1, len(nums)):
            if curr[-1] + numstr[index] > numstr[index] + curr[-1]:
                numstr[index - len(curr)] = numstr[index]
                numstr[index] = curr[-1]
                
            elif curr[-1] + numstr[index] == numstr[index] + curr[-1]:
                curr.append(numstr[index])
                
            else:
                curr = [numstr[index]]
        
        result = ''.join(reversed(numstr)) 
        
        if int(result) > 0:
            return result
        
        else:
            return '0'