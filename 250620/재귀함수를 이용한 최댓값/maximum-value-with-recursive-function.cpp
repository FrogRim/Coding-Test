#include <iostream>

using namespace std;

int n;
int arr[100];
int tmp = 0;

int Maximaize(int n)
{
    if(n == 0)
    {
        return arr[n]; 
    }
    
    return (Maximaize(n-1) < arr[n]) ? arr[n] : Maximaize(n-1);
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