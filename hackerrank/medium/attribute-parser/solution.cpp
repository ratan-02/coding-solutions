#include <iostream>
#include <sstream>
#include <stack>
#include <map>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;
    cin.ignore();

    map<string, string> mp;
    stack<string> st;

    while (n--) {
        string line;
        getline(cin, line);

        if (line.substr(0, 2) == "</") {
            st.pop();
        } else {
            // Remove '<' and '>'
            line = line.substr(1, line.size() - 2);

            stringstream ss(line);
            string tag;
            ss >> tag;

            string path;
            if (st.empty())
                path = tag;
            else
                path = st.top() + "." + tag;

            st.push(path);

            string attr, eq, value;
            while (ss >> attr) {
                ss >> eq;
                ss >> value;

                // Remove quotes
                value = value.substr(1, value.size() - 2);

                mp[path + "~" + attr] = value;
            }
        }
    }

    while (q--) {
        string query;
        getline(cin, query);

        if (mp.find(query) != mp.end())
            cout << mp[query] << endl;
        else
            cout << "Not Found!" << endl;
    }

    return 0;
}
