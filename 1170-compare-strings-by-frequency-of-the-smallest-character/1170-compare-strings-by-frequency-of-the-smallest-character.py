class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def freq(s):
            m = min(s)
            return s.count(m)
        
        for idx, val in enumerate(queries):
             queries[idx] = freq(val)
        
        for idx, val in enumerate(words):
            words[idx] = freq(val)
        
        words.sort()
        
        for idx, val in enumerate(queries):
            queries[idx] = len(words) - bisect_right(words, val)
            
        return queries