class Solution {
    public int minimizeXor(int num1, int num2) {
        int count = 0;
        
        while (num2 != 0) {
            if ((num2 & 1) == 1) count++;
            num2 >>= 1;
        }
        
        int x = 0;
        for (int i = 21; i >= 0 && count > 0; i--) {
            if ((num1 & (1 << i)) != 0) {
                x |= (1<< i);
                count--;
            }
        }

        if (count > 0) {
            for (int i = 0; i < 32 && count > 0; i++) {
                if ((x & (1 << i)) == 0) {
                    x |= (1 << i);
                    count--;
                }
            }
        }

        return x;
    }
}