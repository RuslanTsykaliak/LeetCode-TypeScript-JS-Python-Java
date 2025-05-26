class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        G = defaultdict(set)
        inDeg = [0] * n
        for a, b in edges:
            G[a].add(b)
            inDeg[b] += 1
        Queue = [i for i in range(n) if inDeg[i] == 0]
        dic = {
            i: defaultdict(int) for i in range(n)
        }
        visitCount, ans = 0, 1
        while Queue:
            i = Queue.pop()
            dic[i][colors[i]] += 1
            ans = max(ans, max(dic[i].values()))
            visitCount += 1
            for j in G[i]:
                for x in dic[i]:
                    dic[j][x] = max(dic[i][x], dic[j][x])
                inDeg[j] -= 1
                if inDeg[j] == 0:
                    Queue.append(j)
        return ans if visitCount == n else -1
