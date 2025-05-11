class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Input: an array of integers
        # Output: True or False
        # Conditions: True if the array contains 3 consecutive (one after another) odd numbers
        # False if array contain less than 3 consecutive odd number

        # To solve this we can make easy check if array has more than 2 numbers, if less we can return False imidiately
        if len(arr) < 3:
            return False

        # To store odd numbers we can use integer count
        consecutiveOddCount = 0

        # To check odd numbers we will use for loop and if else
        for n in arr:
            # if odd number found incremenent count by 1
            if n % 2 != 0:
                consecutiveOddCount += 1
                # if else to return True if count of odd numbers reach 3
                if consecutiveOddCount == 3:
                    return True
            # if even number reset count to 0
            else:
                consecutiveOddCount = 0

        # For return statement we put if count more than 3 return True othervise return False
        return False