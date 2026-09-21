class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v,w))
        heap = [(0,k)]
        res = 0 
        visited = set()
        while heap:
            w, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            res = max(res, w)
            for nei, we in adj[n1]:
                heapq.heappush(heap, (w + we, nei))
        return res if len(visited) == n else -1