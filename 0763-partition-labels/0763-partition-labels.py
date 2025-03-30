class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Input: String
        # Constrains: split String so that each letter appears only in one part
        # Output: a list of integers representig the size of these parts
        # Use Hash or array of characters to be able check what character present
        # We can use Sliding Window by creating start and end. The condition of spliting a string from left side to the right and moving whole window and ensure no character in the current window appears in any other partition

        # Sliding Window

        # Calculate the last index
        last_index = {char: idx for idx, char in enumerate(s)}

        partitions = []
        start, end = 0, 0

        for i, char in enumerate(s):
            # Expand the partition
            end = max(end, last_index[char])
            # End of the current partition
            if i == end:
                partitions.append(end - start + 1)
                # Start of the next partition
                start = i + 1

        return partitions
