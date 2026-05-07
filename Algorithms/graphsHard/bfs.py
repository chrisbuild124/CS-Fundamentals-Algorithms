# This problem focuses on stop lights and requires to find the 2nd minimum time to get to destination

# Leetcode link: https://leetcode.com/problems/second-minimum-time-to-reach-destination/

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # No cycles
        # Allowed to go backwards
        # 2nd fastest unique time

        src, dest = 1, n
        INF = float('inf')
        adj = defaultdict(list)
        times = [INF] * n # optimization #1
        changed = [0] * n # optimization #1
        q = deque([src]) # node
        cur_time = 0

        for s, e in edges:
            adj[s].append(e)
            adj[e].append(s)

        while q:
            for _ in range(len(q)):
                if (cur_time // change) % 2:
                    break
                node = q.popleft()
                if node == dest and times[dest - 1] != cur_time and changed[dest - 1] == 2:
                    return cur_time
                
                for nei in adj[node]:
                    if times[nei - 1] != cur_time and changed[nei - 1] < 2:
                        q.append(nei)
                        times[nei - 1] = cur_time
                        changed[nei - 1] += 1
            if (cur_time // change) % 2:
                if dest in q and times[dest - 1] != cur_time and changed[dest - 1] == 2:
                    return cur_time
                cur_time = (cur_time // change + 1) * change
            else:
                cur_time += time
        
