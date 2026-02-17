class Solution {
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> res = new ArrayList<String>();
        for (int i = 0; i < 1024; ++i) {
            int h = i >> 6;
            int m = i & 63; // Extract the high 4 bits and low 6 bits using bitwise operations
            if (h < 12 && m < 60 && Integer.bitCount(i) == turnedOn) {
                res.add(h + ":" + (m < 10 ? "0" : "") +m);
            }
        }
        return res;
    }
}