/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function (nums, head) {
    let currNode = null, startNode = null, numMap = {};

    nums.forEach((num) => {
        numMap[num] = num;
    })

    while (head) {
        if (!(head.val in numMap)) {
            if (startNode) {
                currNode.next = head;
                currNode = currNode.next;
            } else {
                startNode = head;
                currNode = startNode;
            }
        }
        head = head.next;
    }
    if (currNode) {
        currNode.next = null;
    }
    return startNode;
};