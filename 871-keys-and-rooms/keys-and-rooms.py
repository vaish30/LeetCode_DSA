class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        keys = set()
        keys.add(0)
        k = 1
        while k!=0:
            k=len(keys)
            for i in range(n):
                if i in keys:
                    keys.update(rooms[i])
            k = len(keys)-k
        return len(keys)==n