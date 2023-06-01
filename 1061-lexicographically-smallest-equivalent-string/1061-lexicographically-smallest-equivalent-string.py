class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        representative = [i for i in range(26)]
        
        # Returns the root representative of the component.
        def find(x):
            if representative[x] == x:
                return x
            
            representative[x] = find(representative[x])
            return representative[x]
        
        # Perform union if x and y aren't in the same component.
        def performUnion(x, y):
            x = find(x)
            y = find(y)
            
            if x == y:
                return
            
            # Make the smaller character representative.
            if x < y:
                representative[y] = x
            else:
                representative[x] = y
        
        # Make each character representative of itself.
        for i in range(26):
            representative[i] = i
        
        # Perform union merge for all the edges.
        for i in range(len(s1)):
            performUnion(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))
        
        ans = []
        # Create the answer string with final mappings.
        for c in baseStr:
            ans.append(chr(find(ord(c) - ord('a')) + ord('a')))
        
        return "".join(ans)
