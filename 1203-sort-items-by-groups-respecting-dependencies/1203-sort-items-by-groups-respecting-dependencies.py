class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for item in range(n):
            if group[item]==-1:
                group[item]=m
                m+=1

        visited=set()

        indegree_items=[0]*n #num of incoming edges for item
        outdegree_items=defaultdict(set) #num of outgoing edges for item

        indegree_groups=[0]*m #num of incoming edges for a group
        outdegree_groups=defaultdict(set) #num of outgoing edges for a group

        # filling incoming and outgoing of items and groups
        for i,b in enumerate(beforeItems):
            for before in b:
                if group[before]==group[i]:
                #if group is same then item will be arranged internally
                    indegree_items[i]+=1
                    outdegree_items[before].add(i)

                #if group are not same then whole group will be arranged
                else:
                    # the group order is already added and cannot increase indegree again
                    if (group[i],group[before]) in visited: 
                        continue

                    visited.add((group[i],group[before]))

                    indegree_groups[group[i]]+=1
                    outdegree_groups[group[before]].add(group[i])

        groups=[[] for _ in range(m)]# creating group:[items] array

        for i in range(n):
            groups[group[i]].append(i)


        # sorting items in groups
        for gnum,grp in enumerate(groups):
            q=deque()

            for item in grp:
                if indegree_items[item]==0:# starting with loose ends i.e no incoming edges
                    q.append(item)

            cursorted=[] #storing the cur sorting

            while q:
                current=q.popleft()
                cursorted.append(current)

                for outgoin in outdegree_items[current]:#checking outgoin edges from here
                    indegree_items[outgoin]-=1
                    
                    if indegree_items[outgoin]==0:
                        q.append(outgoin)
        #if the len is unequal that means the edges are not connected and did not sort all items
            if len(cursorted)!=len(grp):
                return []

            groups[gnum]=cursorted #replacing with sorted one

        #sorting groups
        q=deque()

        for grp,num in enumerate(indegree_groups):
            if num==0: # start with loose ends
                q.append(grp)

        res=[]

        while q:
            curgroup=q.popleft()

            for item in groups[curgroup]:#add all sorted items of cur group
                res.append(item)

            for outgoin in outdegree_groups[curgroup]:#check outgoin edge for group
                indegree_groups[outgoin]-=1
                
                if indegree_groups[outgoin]==0:
                    q.append(outgoin)

        if len(res) != n:#that means groups sorted fully
            return []

        return res


        # Time: O(4n+m+2nlogn)   -- nlogn for pushpop in queue
        # Space ~~ O(7n)