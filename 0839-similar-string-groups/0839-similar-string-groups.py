class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        #dedupe input
        strs=list(set(strs))

        parents=list(range(len(strs)))
        size=[1]*len(strs)

        wordlen=len(strs[0])

        def similar(word1,word2):
            diff=i=0
            
            while i<wordlen and diff<=2:
                if word1[i]!=word2[i]:
                    
                    diff+=1

                i+=1

            return diff<=2

        def find(a):
            if parents[a]!=a:
                #path compression
                parents[a]=parents[parents[a]]
                a=parents[a]

            return parents[a]

        def union(a,b):
            a,b=find(a),find(b)
            
            if a==b:
                return 
            
            #swap so a is larger, as we will make a parent
            if size[a]<size[b]:
                a,b=b,a

            size[a]+=size[b]
            parents[b]=a


        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                
                if similar(strs[i],strs[j]):
                    
                    union(i,j)

        #count parents who are roots(their own parent)
        return sum([1 for i,e in enumerate(parents) if i==e])  