class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        for pos, vel in sorted(zip(position, speed))[::-1]:
            distance = target - pos
            
            if not stack:
                stack.append(distance / vel)
        
            elif distance / vel > stack[-1]:
                stack.append(distance / vel)
            
        return len(stack)