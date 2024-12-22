from heapq import *

class Solution:
    def leftmostBuildingQueries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        # To store the results for each query
        result = [-1] * len(queries)
        # To group deferred queries by building `bob`
        qs = [[] for _ in range(len(heights))]

        for index, (alice, bob) in enumerate(queries):
            # Ensure `alice` is the smaller index for consistency
            if alice > bob:
                alice, bob = bob, alice

            # Directly solvable queries
            if alice == bob or heights[alice] < heights[bob]:
                result[index] = bob
            else:
                # Defer the query for processing later
                qs[bob].append((heights[alice], index))

        # Min-heap to process deferred queries efficiently
        min_heap = []

        # Iterate through each building
        for index, height in enumerate(heights):
            # Add deferred queries related to this building
            for q in qs[index]:
                heappush(min_heap, q)

            # Process the heap for this building
            while min_heap and min_heap[0][0] < height:
                # Remove satisfied queries
                _, query_index = heappop(min_heap)
                # Update result with the current building
                result[query_index] = index

        return result
