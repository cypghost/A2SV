class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # initialize data structures + result list
        in_degrees = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        queue = collections.deque()
        result = []
        
        # supplies are our sources - no in degrees
        for supply in supplies:
            in_degrees[supply] = 0
            # because supplies are our sources to start, add to queue
            queue.append(supply)
        
        
        # add recipes/ingredients
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                in_degrees[recipe] += 1
        
        # queue starts off with supplies(our sources with no in degrees)
        # we pop off from queue and check if it is a recipe
        # if it is, this means we can create it so add to our result
        # we remove the edges going into other neighbors since we are done processing
        # if the neighbor has no in degrees(no incoming edges) it becomes a source and we add to queue
        while queue:
            node = queue.popleft()
            # check if this is a recipe - if it is we can make it
            if node in recipes:
                result.append(node)
            
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1
                
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
            
        return result
