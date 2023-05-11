class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        res = []
        
        for key in freq:
            res.append((-freq[key], key))
        
        heapify(res)
        ans = []
        
        for index in range(k):
            val = heappop(res)
            ans.append(val[1])
        
        return ans
        
        
        
        