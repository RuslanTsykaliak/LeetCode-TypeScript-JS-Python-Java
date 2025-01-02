class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Get the total number of words in the input list
        n = len(words)

        # Define a set of vowels for quick lookup
        vowel = {"a", "e", "i", "o", "u"}

        # Create a prefix sum array to store cumulative counts of valid strings
        prefix = [0] * (n + 1)

        # Populate the prefix sum array
        for i in range(n):
            curr = words[i]
            # Check if the current word starts and ends with a vowel
            if curr[0] in vowel and curr[-1] in vowel:
                # Increment the cumulative count for valid strings
                prefix[i + 1] = prefix[i] + 1
            else:
                # Carry forward the count without increment
                prefix[i + 1] = prefix[i]

        # Initialize a result list to store answers for each query
        result = []

        # Process each query range [l, r]
        for l, r in queries:
            # Calculate the number of valid strings in the range using prefix sums
            result.append(prefix[r + 1] - prefix[l])

        # Return the list of results for all queries
        return result
