class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()  # Sort the numbers to check divisibility easily

        # res: Key = path length, Value = list of paths of that length
        res = collections.defaultdict(list)
        res[1].append([nums[0]])  # First number starts a path of length 1
        max_len = 1  # Track the length of the longest path found

        for i in range(1, len(nums)):
            num = nums[i]  # Current number to potentially add
            added = False  # Track if 'num' was added to any path

            # Check existing paths, from longest to shortest
            for length in range(max_len, 0, -1):
                for path in res[length]:
                    if num % path[-1] == 0:  # Check divisibility rule
                        new_path = path + [num]  # Add 'num' to the path
                        new_len = length + 1
                        res[new_len].append(new_path)  # Record the new path

                        if new_len > max_len:  # Update max length found
                            max_len = new_len

                        added = True
                        break  # Stop checking paths at this length
                if added:
                    break  # Stop checking shorter lengths

            if not added:  # If 'num' couldn't extend any path
                res[1].append([num])  # Start a new path of length 1

        return res[max_len][0]  # Return any path with the maximum length
