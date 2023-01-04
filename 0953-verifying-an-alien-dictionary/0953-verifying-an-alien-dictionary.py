class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # dictionary to contain the alpahbet and new order for comparison
        alphabet = {}
        neworder =[]
        # append the alphabet
        for index, char in enumerate(order):
            alphabet[char] = index
        # append to neworder to compare
        for word in words:
            new = []
            for char in word:
                new.append(alphabet[char])
            neworder.append(new)
        # Compare the letters if they is an alien language
        for char, letter in zip(neworder, neworder[1:]):
            if char > letter:
                return False
            
        return True
                