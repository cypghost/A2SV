class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        incoming = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)
            incoming[b] += 1

        todo = []

        for index in range(numCourses):
            if incoming[index] == 0:
                todo.append(index)

        order = [[] for _ in range(numCourses)]

        while todo:
            curr = todo.pop(0)

            for neighbor in graph[curr]:
                for index in order[curr]:
                    if index not in order[neighbor]:
                        order[neighbor].append(index)

                order[neighbor].append(curr)
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    todo.append(neighbor)

        ans = []

        for a, b in queries:
            if a in order[b]:
                ans.append(True)

            else:
                ans.append(False)

        return ans