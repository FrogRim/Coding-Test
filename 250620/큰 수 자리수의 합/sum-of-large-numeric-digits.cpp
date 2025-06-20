#include <iostream>

using namespace std;

int a, b, c;

int F(int n) {
    if(n < 10)
        return n;

    return F(n / 10) + (n % 10);
}


int main() {
    cin >> a >> b >> c;

    // Please write your code here.
    int num = a*b*c;

    cout << F(num);

    return 0;
}