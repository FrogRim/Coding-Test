#include <iostream>
#include <algorithm>
using namespace std;

int n;
int A[100];
int B[100];

bool flag = true;
int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    sort(A,A+n);

    for (int i = 0; i < n; i++) {
        cin >> B[i];
    }
    sort(B,B+n);
    // Please write your code here.
    for(int i = 0; i < n; i++)
    {
        if(A[i] != B[i])
        {
            flag = false;
            break;
        }
    }

    if(flag ==true)
        cout<< "Yes";
    else
        cout<< "No";

    return 0;
}