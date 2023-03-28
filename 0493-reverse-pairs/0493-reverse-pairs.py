class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def mergesort(nums, left, right):
            
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            
            inv = mergesort(nums, left, mid) 
            inv += mergesort(nums, mid + 1, right)
            inv += merge(nums, left, right, mid)
            
            return inv
        
        def merge(nums, left, right, mid):
            count = 0
            r = mid + 1
            
            for index in range(left, mid + 1):
                while r <= right and nums[index] > 2 * nums[r]:
                    r += 1
                    
                count += (r - (mid + 1))
            
            left_ptr = left
            right_ptr = mid + 1
            merged = []
            
            while left_ptr <= mid and right_ptr <= right:
                if nums[left_ptr] <= nums[right_ptr]:
                    merged.append(nums[left_ptr])
                    left_ptr += 1
                
                else:
                    merged.append(nums[right_ptr])
                    right_ptr += 1
            
            merged += nums[left_ptr : mid + 1]
            merged += nums[right_ptr : right + 1]
            
            for index in range(left, right + 1):
                nums[index] = merged[index - left]
                
            return count
        
        return mergesort(nums, 0, len(nums) - 1)
   