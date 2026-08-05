#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

vector<int> parseInts(string str) {
    vector<int> result;
    stringstream ss(str);

    int num;
    char comma;

    while (ss >> num) {
        result.push_back(num);
        ss >> comma;
    }

    return result;
}

int main() {
    string str;
    cin >> str;

    vector<int> integers = parseInts(str);

    for (int i = 0; i < integers.size(); i++) {
        cout << integers[i] << endl;
    }

    return 0;
}
