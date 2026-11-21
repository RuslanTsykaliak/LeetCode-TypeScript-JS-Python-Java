class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        first_child, next_sibling = [-1] * n, [
            -1
        ] * n  # Children as a linked list in two int arrays

        for x in range(n - 1, 0, -1):
            next_sibling[x] = first_child[parent[x]]
            first_child[parent[x]] = x
        size, last = [
            1
        ] * n, {}  # last[c]: the deepest node with letter c on the path from the root

        def dfs(x: int) -> None:
            c = s[x]
            above = last.get(c, -1)  # The closest ancestor with the same letter, or -1
            last[c] = x
            child = first_child[x]
            while child != -1:
                dfs(child)
                child = next_sibling[child]
            last[c] = above
            if x:  # The root has no parent
                size[above if above >= 0 else parent[x]] += size[x]

        dfs(0)
        return size
