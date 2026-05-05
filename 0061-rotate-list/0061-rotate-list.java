/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) {
            return head;
        }

        int len = 0;
        ListNode temp = head;

        while (temp != null) {
            len++;
            temp = temp.next;
        }

        int[] arr = new int[len];
        temp = head;
        int x = 0;
        while (temp != null) {
            arr[x++] = temp.val;
            temp = temp.next;
        }

        k = k % len;
        reverseArr(arr, 0, len - 1);
        reverseArr(arr, 0, k - 1);
        reverseArr(arr, k, len - 1);

        ListNode ans = new ListNode(0);
        temp = ans;
        x = 0;
        while (x < len) {
            ListNode node = new ListNode(arr[x++]);
            temp.next = node;
            temp = temp.next;
        }
        temp.next = null;
        return ans.next;
    }

    public void reverseArr(int[] nums, int start, int last) {
        while (start < last) {
            int temp = nums[start];
            nums[start] = nums[last];
            nums[last] = temp;
            start++;
            last--;
        }
    }
}