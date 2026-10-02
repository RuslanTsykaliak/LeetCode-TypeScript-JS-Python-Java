class Solution {
    List<String> res;

    private void f(int left, int right, StringBuilder curr) {
        if (left == 0 && right == 0) {
            res.add(new String(curr));
        }
        if (left > 0) {
            curr.append('(');
            f(left - 1, right, curr);
            curr.deleteCharAt(curr.length() - 1);
        }
        if (right > 0 && right > left) {
            curr.append(')');
            f(left, right - 1, curr);
            curr.deleteCharAt(curr.length() - 1);
        }
    }

    public List<String> generateParenthesis(int n) {
        res = new ArrayList<>();
        f(n, n, new StringBuilder());
        return res;
    }
}