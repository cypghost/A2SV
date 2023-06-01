class Disjoint:
    def __init__(self):
        self.rank = [0] * 26
        self.parent = [index for index in range(26)]

    def finduPar(self, node):
        if self.parent[node] == node:
            return node

        self.parent[node] = self.finduPar(self.parent[node])

        return self.parent[node]

    def byrank(self, u, v):
        root_u = self.finduPar(u)
        root_v = self.finduPar(v) 
 
        if root_u == root_v:
            return False 

        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u 

        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v  

        else : 
            self.parent[root_v] = root_u
            self.rank[root_u] += 1


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        disjoint = Disjoint()
        nq = []
        n = len(equations)

        for index in range(n):
            if equations[index][1] == '!':
                if equations[index][0] == equations[index][-1]:
                    return False

                else:
                    nq.append(equations[index])
            else:
                disjoint.byrank(ord(equations[index][0]) - 97, ord(equations[index][-1]) - 97)

        for index in range(len(nq)):
            x = ord(nq[index][0]) - 97
            y = ord(nq[index][-1]) - 97

            if disjoint.finduPar(x) == disjoint.finduPar(y):
                return False

        return True