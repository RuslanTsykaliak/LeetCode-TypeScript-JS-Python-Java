import java.util.*;

class Solution {
    // Segment Tree Arrays
    private int[] count;
    private long[] len;
    private int[] xCoords;

    public double separateSquares(int[][] squares) {
        // 1. Coordinate Compression for X
        Set<Integer> xSet = new HashSet<>();
        for (int[] sq : squares) {
            xSet.add(sq[0]);
            xSet.add(sq[0] + sq[2]);
        }

        int m = xSet.size();
        xCoords = new int[m];
        int idx = 0;
        for (int x : xSet)
            xCoords[idx++] = x;
        Arrays.sort(xCoords);

        Map<Integer, Integer> xMap = new HashMap<>();
        for (int i = 0; i < m; i++) {
            xMap.put(xCoords[i], i);
        }

        // 2. Create Events (Sweep Line)
        List<Event> events = new ArrayList<>();
        for (int[] sq : squares) {
            int x1 = xMap.get(sq[0]);
            int x2 = xMap.get(sq[0] + sq[2]);
            // type 1 for bottom edge, -1 for top edge
            events.add(new Event(sq[1], 1, x1, x2));
            events.add(new Event(sq[1] + sq[2], -1, x1, x2));
        }
        Collections.sort(events);

        // 3. Segment Tree Initialization
        // We have m unique x-coordinates, creating m-1 elementary intervals.
        // The segment tree covers indices 0 to m-2.
        count = new int[4 * m];
        len = new long[4 * m];

        long totalArea = 0;
        List<Strip> strips = new ArrayList<>();

        // 4. Sweep Line Execution
        for (int i = 0; i < events.size(); i++) {
            Event e = events.get(i);

            // Calculate area added by the previous vertical strip
            if (i > 0) {
                int yPrev = events.get(i - 1).y;
                int yCurr = e.y;
                if (yCurr > yPrev) {
                    long activeWidth = len[1]; // len[1] is the union length from the root
                    long areaChunk = activeWidth * (long) (yCurr - yPrev);
                    totalArea += areaChunk;
                    strips.add(new Strip(yPrev, yCurr, activeWidth));
                }
            }

            // Update Segment Tree
            // The square spans x indices from x1 to x2.
            // The elementary intervals involved are x1 to x2-1.
            if (e.x1 < e.x2) {
                update(1, 0, m - 2, e.x1, e.x2 - 1, e.type);
            }
        }

        // 5. Find the split line
        double target = totalArea / 2.0;
        double currentArea = 0;

        for (Strip s : strips) {
            double stripArea = (double) s.width * (s.yTop - s.yBot);
            if (currentArea + stripArea >= target) {
                // The split line is inside this strip
                double needed = target - currentArea;
                return s.yBot + (needed / s.width);
            }
            currentArea += stripArea;
        }

        // Fallback (should theoretically not be reached with valid input)
        return events.get(events.size() - 1).y;
    }

    // Segment Tree Update
    // node: current tree node
    // start, end: range of elementary intervals covered by this node
    // l, r: update range
    // val: +1 (add square) or -1 (remove square)
    private void update(int node, int start, int end, int l, int r, int val) {
        if (l > end || r < start)
            return;

        if (l <= start && end <= r) {
            count[node] += val;
        } else {
            int mid = start + (end - start) / 2;
            update(node * 2, start, mid, l, r, val);
            update(node * 2 + 1, mid + 1, end, l, r, val);
        }
        pushUp(node, start, end);
    }

    // Recalculate covered length for the node
    private void pushUp(int node, int start, int end) {
        if (count[node] > 0) {
            // If count > 0, the whole range [start, end] is covered.
            // Physical length is xCoords[end+1] - xCoords[start]
            len[node] = xCoords[end + 1] - xCoords[start];
        } else {
            // If count == 0, length is the sum of children (unless it's a leaf)
            if (start == end) {
                len[node] = 0;
            } else {
                len[node] = len[node * 2] + len[node * 2 + 1];
            }
        }
    }

    // Helper class for Sweep Line Events
    private static class Event implements Comparable<Event> {
        int y, type, x1, x2;

        public Event(int y, int type, int x1, int x2) {
            this.y = y;
            this.type = type;
            this.x1 = x1;
            this.x2 = x2;
        }

        public int compareTo(Event other) {
            return Integer.compare(this.y, other.y);
        }
    }

    // Helper class to store processed vertical strips
    private static class Strip {
        int yBot, yTop;
        long width;

        public Strip(int yBot, int yTop, long width) {
            this.yBot = yBot;
            this.yTop = yTop;
            this.width = width;
        }
    }
}