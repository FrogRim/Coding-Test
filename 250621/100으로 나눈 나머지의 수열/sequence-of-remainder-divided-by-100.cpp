#include <iostream>

using namespace std;

int N;

int f(int n)
{
    if(n == 1)
        return 2;
    
    if(n == 2)
        return 4;

    
    return (f(n-1) * f(n-2))%100;
}

int main() {
    cin >> N;

    // Please write your code here.

    cout<< f(N);
    return 0;
}