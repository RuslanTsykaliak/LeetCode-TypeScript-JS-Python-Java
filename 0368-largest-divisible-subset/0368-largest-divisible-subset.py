class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        # Sort the stones (numbers) to process them in increasing order
        nums.sort()

        # Dictionary to store pyramids grouped by their height (length)
        # Key: height (int)
        # Value: list of pyramids (List[List[int]]) with that height
        pyramids_by_height = collections.defaultdict(list)

        # The first stone forms the first pyramid of height 1
        pyramids_by_height[1].append([nums[0]])
        max_height = 1

        # Process the rest of the stones
        for i in range(1, n):
            current_num = nums[i]
            was_added = False # Flag to check if current_num extended any pyramid

            # Try to place current_num on top of existing pyramids
            # Check from the tallest pyramids downwards (prioritize extending taller ones)
            for height in range(max_height, 0, -1):
                # Look at all pyramids currently at this height
                for pyramid in pyramids_by_height[height]:
                    top_stone = pyramid[-1] # The last stone added to this pyramid

                    # Check the rule: Can current_num go on top_stone?
                    if current_num % top_stone == 0:
                        # Yes! Extend this pyramid
                        new_pyramid = pyramid + [current_num]
                        new_height = height + 1

                        # Add the new, taller pyramid to our records
                        pyramids_by_height[new_height].append(new_pyramid)

                        # Update the overall max_height if this is a new record
                        if new_height > max_height:
                            max_height = new_height

                        # Mark that we added the stone and stop searching for this current_num
                        was_added = True
                        break # Stop checking other pyramids at this height
                
                if was_added:
                    break # Stop checking pyramids of lower heights

            # If current_num couldn't be added on top of ANY existing pyramid
            if not was_added:
                # It starts its own new pyramid of height 1
                pyramids_by_height[1].append([current_num])

        # Return any one of the pyramids with the maximum height
        # The user's original code returned the first one found ([0])
        return pyramids_by_height[max_height][0]