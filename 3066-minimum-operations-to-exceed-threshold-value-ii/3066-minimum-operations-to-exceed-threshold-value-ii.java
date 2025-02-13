import java.util.PriorityQueue;

class Solution {
    public int minOperations(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for (int num : nums) {
            minHeap.offer(num);
        }
        int numOperations = 0;

        while (minHeap.peek() < k) {
            int x = minHeap.poll();
            int y = minHeap.poll();
            minHeap.offer(x * 2 + y);
            numOperations++;
        }
        return numOperations;
    }
}
