class Solution:
    def isRobotBounded(self, s: str) -> bool:
        n, a, b = len(s), 0, 0
        directions = "N"
        for j in range(100):
            for i in range(n):
                if s[i] == "G":
                    if directions == "N":
                        b += 1

                    elif directions == "S":
                        b -= 1

                    elif directions == "E":
                        a += 1

                    else:
                        a -= 1

                elif s[i] == "L":
                    if directions == "N":
                        directions = "W"

                    elif directions == "S":
                        directions = "E"

                    elif directions == "E":
                        directions = "N"

                    else:
                        directions = "S"

                elif s[i] == "R":
                    if directions == "N":
                        directions = "E"

                    elif directions == "S":
                        directions = "W"

                    elif directions == "E":
                        directions = "S"

                    else:
                        directions = "N"
                         
            if a == b == 0:
                return True
    
        return False