#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string fizzBuzz(int n) {
        if (n % 3 == 0 && n % 5 == 0)
            return "FizzBuzz";
        else if (n % 3 == 0)
            return "Fizz";
        else if (n % 5 == 0)
            return "Buzz";
        else
            return to_string(n);
    }
};

int main() {
    int n;
    cin >> n;

    Solution obj;
    cout << obj.fizzBuzz(n);

    return 0;
}