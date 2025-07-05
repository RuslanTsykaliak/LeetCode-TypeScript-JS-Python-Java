class Solution(object):
    def findLucky(self, arr):
        x = Counter(arr)
        high = -1
        for item, value in x.items():
            if item == value:
                high = max(value, high)
        return high