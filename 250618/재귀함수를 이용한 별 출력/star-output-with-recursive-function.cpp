#include <iostream>

using namespace std;

int n;

void Print_star(int n){
    if(n == 0){
        return;
    }
    
    Print_star(n-1);
    for(int i=0; i < n; i++){
        cout <<'*';
    }
    cout<<endl;
    
}

int main() {
    cin >> n;

    // Please write your code here.
    Print_star(n);
    return 0;
}