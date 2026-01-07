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
class Solution {
    private static final int MOD = 1_000_000_007;
    private long totalSum = 0;
    private long maxProduct = 0;

    public int maxProduct(TreeNode root) {
        // First DFS: compute total sum
        totalSum = dfsSum(root);

        // Second DFS: compute max product
        dfsMaxProduct(root);

        return (int) (maxProduct % MOD);
    }

    private long dfsSum(TreeNode node) {
        if (node == null)
            return 0;
        return node.val + dfsSum(node.left) + dfsSum(node.right);
    }

    private long dfsMaxProduct(TreeNode node) {
        if (node == null)
            return 0;

        long leftSum = dfsMaxProduct(node.left);
        long rightSum = dfsMaxProduct(node.right);

        long subtreeSum = node.val + leftSum + rightSum;

        maxProduct = Math.max(
                maxProduct,
                subtreeSum * (totalSum - subtreeSum));

        return subtreeSum;
    }
}