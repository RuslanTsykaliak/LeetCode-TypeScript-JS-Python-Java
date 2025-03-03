/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

// Function to detect whether a singly-linked list has a cycle.
// This uses Floyd's Tortoise and Hare algorithm.
function hasCycle(head: ListNode | null): boolean {
    // Initialize two pointers, 'slowPointer' and 'fastPointer' at the head of the list.
    let slowPointer = head;
    let fastPointer = head;

    // Traverse the list with both pointers.
    while (fastPointer !== null && fastPointer.next !== null) {
        // Move 'slowPointer' one step.
        slowPointer = slowPointer.next;
        // Move 'fastPointer' two steps.
        fastPointer = fastPointer.next.next;

        // If 'slowPointer' and 'fastPointer' meet, a cycle is detected.
        if (slowPointer === fastPointer) {
            return true;
        }
    }
  
    // If 'fastPointer' reaches the end of the list, no cycle is present.
    return false;
}