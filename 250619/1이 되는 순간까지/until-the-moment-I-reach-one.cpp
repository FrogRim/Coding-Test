#include <iostream>

using namespace std;

int N;


int F(int n,int cnt) {

    if(n == 1) {
        return cnt;
    }

    
    if(n % 2 == 0){
       
        return F((n/2), cnt+1);
    }
    else{
        
        return F(n/3,cnt+1);
    }
}

int main() {
    cin >> N;
    cout << F(N,0);
    return 0;
}

