#include <iostream>

using namespace std;

int n;
int arr[50];

void Modify(int x[], int size) {
    for (int i = 0; i < size; i++) {
        if (x[i] % 2 == 0) {
            x[i] /= 2;
        }
    }
}


int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.

    Modify(arr,n);

    for (auto q : arr){
        if(q == 0){
            break;
        }
        cout << q <<" ";
    }
    return 0;
}