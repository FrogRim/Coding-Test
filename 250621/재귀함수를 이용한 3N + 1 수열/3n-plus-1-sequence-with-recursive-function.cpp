#include <iostream>

using namespace std;

int n;

int f(int n,int cnt)
{
    if(n == 1)
    {
        return cnt;
    }

    if(n % 2 == 0)
    {
        return f(n/2,cnt+1);
    }
    else
    {
        return f(3*n+1,cnt+1);
    }
}

int main() {
    cin >> n;

    // Please write your code here.
    cout << f(n,0);
    return 0;
}