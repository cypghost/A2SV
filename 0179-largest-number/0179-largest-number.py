class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string = sorted([str(num) for num in nums])
        curr = [string[0]]

        for index in range(1, len(nums)):
            if curr[-1] + string[index] > string[index] + curr[-1]:
                string[index - len(curr)] = string[index]
                string[index] = curr[-1]
                
            elif curr[-1] + string[index] == string[index] + curr[-1]:
                curr.append(string[index])
                
            else:
                curr = [string[index]]
        
        result = ''.join(reversed(string)) 
        
        if int(result) > 0:
            return result
        
        else:
            return '0'