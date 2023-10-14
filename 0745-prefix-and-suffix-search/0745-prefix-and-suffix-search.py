class WordFilter:

    def __init__(self, words: List[str]):
        n = len(words)
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        seen = set()
        
        for index in range(len(words) - 1, -1, -1):
            word = words[index]
            
            if word in seen: continue
                
            seen.add(word)
            
            for i in range(0, len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]
                
                self.prefixes[prefix].add(index)
                self.suffixes[suffix].add(index)
                

    def f(self, pref: str, suff: str) -> int:
        if pref in self.prefixes and suff in self.suffixes:
            indexes = self.prefixes[pref] & self.suffixes[suff]
            
            return max(indexes) if indexes else -1
        
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)