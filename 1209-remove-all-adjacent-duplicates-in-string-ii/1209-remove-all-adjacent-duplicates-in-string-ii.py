# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isEndofWord = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word: str) -> None:
#         node = self.root

#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
            
#             node = node.children[char]
        
#         node.isEndofWord = True
    
#     def search(self, word: str) -> bool:
#         node = self.root

#         for char in word:
#             if char not in node.children:
#                 return False
        
#         return self.isEndofWord
    
#     def startsWith(self, word: str) -> bool:
#         node = self.root

#         for char in word:
#             if char not in node.children:
#                 return False
        
#         return True

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:        
        stack = [['', 0]]    

        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1 

                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([c, 1])            
        
        return ''.join(c * count for c, count in stack)
            
        

        