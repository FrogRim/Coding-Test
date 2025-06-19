#include <iostream>

using namespace std;

int N;

int Fact(int n)
{
    if(n == 0){
        return 1;
    }
    if(n == 1){
        return 1;
    }
    if(n == 2){
        return 2;
    }

    return Fact(n-1) * n;
}
int main() {
    cin >> N;

    // Please write your code here.
    cout << Fact(N);
    return 0;
}