class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def postocord(pos):
            r = (pos - 1) // length
            c = (pos - 1) % length
            if r % 2 == 1:
                c = length - 1 - c
            return [r, c]

        q = deque()
        # pos, moves --> cord, moves
        q.append([1, 0])
        visit = set()
        while q:
            pos, moves = q.popleft()
            for i in range(1, 7):
                nextpos = pos + i
                r, c = postocord(nextpos)
                if board[r][c] != -1:
                    nextpos = board[r][c]
                if nextpos == length * length:
                    return moves + 1
                if nextpos not in visit:
                    visit.add(nextpos)
                    q.append([nextpos, moves + 1])
        return -1
