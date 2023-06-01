class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if 5 not in bills:
            return False

        fivechange = 0
        tenchange = 0
        
        for bill in bills:
            if bill == 5:
                fivechange += 1
            
            elif bill == 10:
                if not fivechange:
                    return False
                
                fivechange -= 1
                tenchange += 1
            
            else:
                if fivechange and tenchange:
                    fivechange -= 1
                    tenchange -= 1
                
                elif fivechange >= 3:
                    fivechange -= 3
                
                else:
                    return False

        return True
                

            
            