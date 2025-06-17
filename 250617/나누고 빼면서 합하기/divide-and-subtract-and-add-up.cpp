#include <iostream>

using namespace std;

int n, m;
int A[100];

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    // Please write your code here.
    int tmp = m;
    int result = 0;

    while(tmp > 0){
        if(tmp % 2 == 0){
            result += A[tmp-1];
            tmp /= 2;
        }
        else{
            result += A[tmp-1];
            tmp -= 1;
        }
                
    }
    cout << result;

    return 0;
}