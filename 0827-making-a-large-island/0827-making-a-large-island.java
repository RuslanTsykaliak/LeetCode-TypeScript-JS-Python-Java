class Solution {
public int largestIsland(int[][] grid) {
        int n = grid.length;
        UnionFind uf = new UnionFind(n * n);
        int[] countMap = new int[n * n];
        boolean[][] checked = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && !checked[i][j]) {
                    bypass(i, j, grid, checked, uf, countMap);
                }
            }
        }
        int max = 0;
        for (int val : countMap) max = Math.max(val, max);
        int[] left = new int[] {1, -1, 0, 0};
        int[] down = new int[] {0, 0, 1, -1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int cur = 1;
                if (grid[i][j] == 0) {
                    Set<Integer> hashes = new HashSet<>();
                    for (int k = 0; k < 4; k++) {
                        int newI = i + left[k];
                        int newJ = j + down[k];

                        if (newI < 0 || newI >= n || newJ < 0 || newJ >= n) continue;

                        int hash = newI * n + newJ;

                        int node = uf.find(hash);
                        if (grid[newI][newJ] == 1 && !hashes.contains(node)) {
                            hashes.add(node);
                            cur += countMap[node];
                        }
                    }
                }
                max = Math.max(max, cur);
            }
        }
        return max;
    }

    public void bypass(int m, int n, int[][] grid, boolean[][] checked, UnionFind uf, int[] countMap) {
        if (checked[m][n]) return;
        checked[m][n] = true;
        int[] up =  new int[] {1, -1, 0, 0};
        int[] left = new int[] {0, 0, 1, -1};
        int curHash = m * grid.length + n;
        int finded = uf.find(curHash);
        countMap[finded] += 1;
        for (int i = 0; i < 4; i++) {
            int newM = m + up[i];
            int newN = n + left[i];
            if (newM < 0 || newN < 0 || newM >= grid.length || newN >= grid.length || grid[newM][newN] != 1 || checked[newM][newN]) {
                continue;
            }
            uf.union(curHash, newM * grid.length + newN);
            bypass(newM, newN, grid, checked, uf, countMap);
        }
    }
    static class UnionFind {
        private final int[] parent;
        private final int[] rank;

        public UnionFind(int size) {
            parent = new int[size];
            rank = new int[size];
            for (int i = 0; i < size; i++) {
                parent[i] = i;
                rank[i] = 1;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        }

        public void union(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) {
                if (rank[rootX] > rank[rootY]) {
                    parent[rootY] = rootX;
                } else if (rank[rootX] < rank[rootY]) {
                    parent[rootX] = rootY;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                }
            }
        }
    }
}