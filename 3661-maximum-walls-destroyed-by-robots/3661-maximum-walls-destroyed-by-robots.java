class Solution {
    public int maxWalls(int[] robots, int[] distance, int[] walls) {
        int n = robots.length;
        int[][] robotDist = new int[n][2];
        for (int i = 0; i < n; i++) {
            robotDist[i][0] = robots[i];
            robotDist[i][1] = distance[i];
        }
        Arrays.sort(robotDist, (a, b) -> a[0] - b[0]);
        Arrays.sort(walls);

        int m = walls.length;
        int rightPtr = 0;
        int leftPtr = 0;
        int curPtr = 0;
        int robotPtr = 0;

        int prevLeft = 0;
        int prevRight = 0;
        int prevNum = 0;
        int subLeft = 0;
        int subRight = 0;

        for (int i = 0; i < n; i++) {
            int robotPos = robotDist[i][0];
            int robotDistVal = robotDist[i][1];

            while (rightPtr < m && walls[rightPtr] <= robotPos) {
                rightPtr++;
            }
            int pos1 = rightPtr;

            while (curPtr < m && walls[curPtr] < robotPos) {
                curPtr++;
            }
            int pos2 = curPtr;

            int leftBound = robotPos - robotDistVal;
            if (i >= 1) {
                leftBound = Math.max(
                        robotPos - robotDistVal,
                        robotDist[i - 1][0] + 1);
            }
            while (leftPtr < m && walls[leftPtr] < leftBound) {
                leftPtr++;
            }
            int leftPos = leftPtr;
            int currentLeft = pos1 - leftPos;

            int rightBound = robotPos + robotDistVal;
            if (i < n - 1) {
                rightBound = Math.min(
                        robotPos + robotDistVal,
                        robotDist[i + 1][0] - 1);
            }
            while (rightPtr < m && walls[rightPtr] <= rightBound) {
                rightPtr++;
            }
            int rightPos = rightPtr;
            int currentRight = rightPos - pos2;

            int currentNum = 0;
            if (i > 0) {
                while (robotPtr < m && walls[robotPtr] < robotDist[i - 1][0]) {
                    robotPtr++;
                }
                int pos3 = robotPtr;
                currentNum = pos1 - pos3;
            }

            if (i == 0) {
                subLeft = currentLeft;
                subRight = currentRight;
            } else {
                int newsubLeft = Math.max(
                        subLeft + currentLeft,
                        subRight -
                                prevRight +
                                Math.min(currentLeft + prevRight, currentNum));
                int newsubRight = Math.max(
                        subLeft + currentRight,
                        subRight + currentRight);
                subLeft = newsubLeft;
                subRight = newsubRight;
            }

            prevLeft = currentLeft;
            prevRight = currentRight;
            prevNum = currentNum;
        }

        return Math.max(subLeft, subRight);
    }
}