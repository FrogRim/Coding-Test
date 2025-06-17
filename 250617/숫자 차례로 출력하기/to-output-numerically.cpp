#include <iostream>

using namespace std;

int N;

void PrintNum(int n)
{
    if (n == 0)
        return;

    PrintNum(n-1);
    cout << n << " ";
}

void PrintNum_reverse(int n)
{
    if (n == 0)
        return;

    PrintNum_reverse(n-1);
    cout << N-(n-1) << " ";
}
int main() {
    cin >> N;

    // Please write your code here.
    PrintNum(N);
    cout << endl;
    PrintNum_reverse(N);

    return 0;
}