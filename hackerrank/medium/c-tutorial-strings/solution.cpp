#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    // Lengths
    cout << a.size() << " " << b.size() << endl;

    // Concatenation
    cout << a + b << endl;

    // Swap first characters
    char temp = a[0];
    a[0] = b[0];
    b[0] = temp;

    cout << a << " " << b << endl;

    return 0;
}
