class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort(reverse=True)

        def can_assign(k: int) -> bool:
            worker_idx = 0
            remaining_pills = pills
            pill_candidates = deque[int]()

            for task_idx in range(k - 1, -1, -1):
                if len(pill_candidates) == 0 and workers[worker_idx] >= tasks[task_idx]:
                    worker_idx += 1
                    continue
                if len(pill_candidates) > 0 and pill_candidates[0] >= tasks[task_idx]:
                    pill_candidates.popleft()
                    continue
                while worker_idx < k and workers[worker_idx] + strength >= tasks[task_idx]:
                    pill_candidates.append(workers[worker_idx])
                    worker_idx += 1
                if len(pill_candidates) > 0 and remaining_pills > 0:
                    pill_candidates.pop()
                    remaining_pills -= 1
                    continue
                return False
            return True

        left, right = 0, min(len(tasks), len(workers))
        max_assignable = 0
        while left <= right:
            mid = (left + right) // 2
            if can_assign(mid):
                max_assignable = mid
                left = mid + 1
            else:
                right = mid - 1

        return max_assignable