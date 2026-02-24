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
    public int sumRootToLeaf(TreeNode root) {
        List<String> res = new ArrayList<>();

        paths(root, res, "");
        int sum = 0;
        for (String r : res) {
            sum += Integer.parseInt(r, 2);
        }
        return sum;
    }

    void paths(TreeNode root, List<String> res, String s) {
        if (root == null) {
            return;
        }
        if (root.right == null && root.left == null) {
            s = s + root.val;
            res.add(s);
        }

        paths(root.left, res, s + root.val);
        paths(root.right, res, s + root.val);
    }
}