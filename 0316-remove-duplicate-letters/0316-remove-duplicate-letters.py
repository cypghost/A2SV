class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occur = {}
        stack = []
        visited = set()

        for index in range(len(s)):
            occur[s[index]] = index

        for index in range(len(s)):

            if s[index] not in visited:
            
                while stack and stack[-1] > s[index] and occur[stack[-1]] > index:
                    visited.remove(stack.pop())

                stack.append(s[index])
                visited.add(s[index])

        return ''.join(stack)