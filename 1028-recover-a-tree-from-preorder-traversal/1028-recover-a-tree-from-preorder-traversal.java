
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

import java.util.AbstractMap.SimpleEntry;

class Solution {
    public TreeNode recoverFromPreorder(String traversal) {
        Stack<SimpleEntry<TreeNode, Integer>> stack = new Stack<>();
        int index = 0;
        TreeNode root = null;

        while (index < traversal.length()) {
            // Count the number of dashes
            int depth = 0;
            while (index < traversal.length()
                    && traversal.charAt(index) == '-') {
                depth++;
                index++;
            }

            // Extract the node value
            int value = 0;
            while (index < traversal.length() &&
                    Character.isDigit(traversal.charAt(index))) {
                value = value * 10 +
                        (traversal.charAt(index) - '0');
                index++;
            }

            // Create the current node
            TreeNode node = new TreeNode(value);

            // If depth is 0, it's the root
            if (depth == 0) {
                root = node;
            } else {
                // Pop nodes from the stack until we find the parent
                while (stack.size() > depth) {
                    stack.pop();
                }

                // Attach the node to the parent
                if (stack.peek().getKey().left == null) {
                    stack.peek().getKey().left = node;
                } else {
                    stack.peek().getKey().right = node;
                }
            }

            // Push the current node and its depth onto the stack
            stack.push(new SimpleEntry<>(node, depth));
        }
        while (stack.size() > 1) {
            stack.pop();
        }

        return stack.peek().getKey();
    }
}