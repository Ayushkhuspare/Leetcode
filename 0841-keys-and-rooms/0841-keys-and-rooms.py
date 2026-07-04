class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {0}
        queue = [0]
        
        while queue:
            current_room = queue.pop(0)
            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
                    
        return len(visited) == len(rooms)
