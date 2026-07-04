class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        # Check if the first node of the first edge is in the second edge
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]

        # Otherwise, the second node must be the center
        return edges[0][1]
