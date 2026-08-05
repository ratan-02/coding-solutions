#include <iostream>
using namespace std;

long long sumMultiples(long long n, long long k) {
    long long m = (n - 1) / k;
    return k * m * (m + 1) / 2;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long n;
        cin >> n;

        cout << sumMultiples(n, 3)
                + sumMultiples(n, 5)
                - sumMultiples(n, 15)
             << endl;
    }

    return 0;
}
