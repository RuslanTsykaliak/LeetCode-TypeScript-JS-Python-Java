class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        int cols = encodedText.length() / rows;
        StringBuilder sb = new StringBuilder();
        int row = 0;
        int col = 0;
        while (col < cols) {
            int i = (row * cols) + col;
            sb.append(encodedText.charAt(i));
            row += 1;
            col += 1;
            if (row == rows) {
                row = 0;
                col -= rows - 1;
            }
        }
        return sb.toString().stripTrailing();
    }
}