#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int n, k;
string t;
string str[100];
vector<string> tmp;



int main() {
    cin >> n >> k >> t;

    for (int i = 0; i < n; i++) {
        
        cin >> str[i];
    }

    for(int i = 0; i < n; i++)
    {
        if (str[i].find(t) == 0) {
            tmp.push_back(str[i]);
        }
        
    }
    // Please write your code here.
    sort(tmp.begin(), tmp.end());

    if (k - 1 < tmp.size()) {
        cout << tmp[k - 1] << '\n';
    }

    return 0;
}