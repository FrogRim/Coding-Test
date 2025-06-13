#include <iostream>

using namespace std;

int n;
int arr[50];

void Modify(int arr[],int n)
{
    for(int i = 0; i <n; i++){
        if(arr[i] < 0){
            arr[i] +=(arr[i]*-2);
        }
        cout<< arr[i] <<" ";
    }
    
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Please write your code here.
    Modify(arr,n);
    return 0;
}

