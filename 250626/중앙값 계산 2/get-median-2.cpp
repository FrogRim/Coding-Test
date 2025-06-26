#include <iostream>
#include<algorithm>
#include<vector>

using namespace std;

int n;
int arr[100];
vector<int> result;

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    

    for (int i = 0; i < n; i ++) {
        
        result.push_back(arr[i]);
        sort(result.begin(),result.end());

        if(i % 2 == 0){
            cout << result[result.size()/2]<<" ";
        }

    }

    return 0;
}