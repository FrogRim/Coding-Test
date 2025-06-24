#include <iostream>

using namespace std;

int n;
int arr[10];


int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}


int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}


int lcmArray(int index) {
    if (index == 0) return arr[0];
    return lcm(lcmArray(index - 1), arr[index]);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << lcmArray(n - 1);
    return 0;
}