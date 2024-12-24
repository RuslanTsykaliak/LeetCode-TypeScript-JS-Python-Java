class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # Step 1: Build the graph (adjacency list) from the edges
        n = len(edges) + 1  # Number of nodes is one more than the number of edges
        graph = {
            i: set() for i in range(n)
        }  # Create a dictionary to store the neighbors of each node

        # Add the edges to the graph
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Helper function: Perform a DFS (depth-first search) to find the farthest node from a given node
        seen = [0] * n  # Keeps track of visited nodes

        def dfs(node):
            if seen[node]:  # If the node is already visited, return an empty path
                return []

            seen[node] = 1  # Mark the node as visited
            longest_path = []  # Store the longest path found so far

            # Explore all neighbors of the current node
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    path_from_neighbor = dfs(
                        neighbor
                    )  # Get the path starting from this neighbor
                    if len(path_from_neighbor) > len(
                        longest_path
                    ):  # If it's longer than the current best path, update
                        longest_path = path_from_neighbor

            # Add the current node to the longest path and return
            longest_path.append(node)
            seen[node] = 0  # Unmark the node as visited (for other potential paths)
            return longest_path

        # Step 2: Find the diameter by running DFS twice
        farthest_node = dfs(0)[0]  # Find the farthest node from node 0
        longest_path = dfs(
            farthest_node
        )  # Find the farthest node from the farthest node

        return max(
            len(longest_path) - 1, 0
        )  # The length of the longest path is the diameter of the tree

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        # Step 3: Get the diameters of both trees
        diameter1 = self.treeDiameter(edges1)
        diameter2 = self.treeDiameter(edges2)

        # Step 4: Calculate the minimum possible diameter after merging
        # It can be the max of the two diameters, or a combination of the two trees' halves
        combined_diameter = (diameter1 + 1) // 2 + (diameter2 + 1) // 2 + 1

        # Return the minimum of the three possible diameters
        return max(diameter1, diameter2, combined_diameter)
