class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            for j in range(i+1, N):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] -points[j][1])
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        # Prim's algorithm 
        heap = [(0,0)]
        res = 0 
        visited = [False] * N
        edges = 0
        while edges < N:
            cost, node = heapq.heappop(heap)
            if visited[node]:
                continue
            visited[node] = True
            edges += 1
            res += cost 
            for nei, dist in adj[node]:
                if not visited[nei]:
                    heapq.heappush(heap, (dist, nei))
        return res

            
