class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        keys = deque([0])
        open_rooms = set()
        
        while keys and len(open_rooms) < n:
            key = keys.popleft()
            open_rooms.add(key)
            
            for room in rooms[key]:
                if room not in open_rooms:
                    keys.append(room)
                    
        return len(open_rooms) == n