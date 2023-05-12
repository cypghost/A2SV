class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0] * numCourses
        
        for requisites in prerequisites:
            a, b = requisites
            graph[a].append(b)
        
        print(graph)
            
        todo = deque([])
        
        for index, count in enumerate(incoming):
            if count == 0:
                todo.append(index)
            
        def cyclefinder(current_course):
            if color[current_course] == 2:
                return False
            
            if color[current_course] == 1:
                return True
            
            color[current_course] = 1
            
            for todos in graph[current_course]:
                cycle_found = cyclefinder(todos)
                
                if cycle_found:
                    return True
            
            color[current_course] = 2
            return False
        
             
        color = [0] * numCourses
        
        for current_todo in todo:
            cycle_found = cyclefinder(current_todo)
            
            if cycle_found:
                return False
        
        return True
            