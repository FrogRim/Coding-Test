#include <iostream>
#include <string>

using namespace std;

string A;

string Check(string A){
    
    char a = A[0];
    for(auto k: A){
        if(k != a){
            return "Yes";
        }
    }
    return "No";
}
int main() {
    cin >> A;

    // Please write your code here.
    cout<< Check(A);
    return 0;
}