class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse=True)

        def can_solve(k: int) -> bool:
            w = 0
            p = pills
            q = deque[int]()
            for t in range(k - 1, -1, -1):
                if len(q) == 0 and workers[w] >= tasks[t]:
                    w += 1
                    continue
                if len(q) > 0 and q[0] >= tasks[t]:
                    q.popleft()
                    continue
                while w < k and workers[w] + strength >= tasks[t]:
                    q.append(workers[w])
                    w += 1
                if len(q) > 0 and p > 0:
                    q.pop()
                    p -= 1
                    continue
                return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        closest = 0
        while left <= right:
            mid = (left + right) // 2
            if can_solve(mid):
                closest = mid
                left = mid + 1
            else:
                right = mid - 1

        return closest