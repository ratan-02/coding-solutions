class Solution {
public:
    int smallestNumber(int n, int t) {
        while (true) {
            int x = n;

            int p = n / 100;
            int q = (n / 10) % 10;
            int r = n % 10;

            int multi;

            if (p == 0) {
                if (n < 10)
                    multi = r;
                else
                    multi = q * r;
            } else {
                multi = p * q * r;
            }

            if (multi % t == 0) {
                return x;
            }

            n++;
        }
    }
};