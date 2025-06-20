#include <iostream>

using namespace std;

int n;
int arr[100];
int tmp = 0;

int Maximaize(int n)
{
    if (n == 0)
        return arr[0];

    int prevMax = Maximaize(n - 1);
    return (arr[n] > prevMax) ? arr[n] : prevMax;
}


int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    cout<< Maximaize(n-1);

    return 0;
}