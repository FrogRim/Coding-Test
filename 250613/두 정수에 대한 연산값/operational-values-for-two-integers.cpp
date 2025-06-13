#include <iostream>
#include<algorithm>

using namespace std;

int a, b;

void Modify(int &a, int &b)
{
    if(a > b){
        a += 25;
        b *= 2;
    }
    else{
        a *=2;
        b += 25;
    }
    cout<< a <<" "<< b;
    
}
int main() {
    cin >> a >> b;

    // Please write your code here.
    Modify(a,b);

    return 0;
}