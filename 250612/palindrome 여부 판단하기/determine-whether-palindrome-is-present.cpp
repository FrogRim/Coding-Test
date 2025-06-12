#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string A;

bool Modify(string &s) {
     string a = s;
     reverse(a.begin(),a.end());
     if(s == a){
        return true;
     }
     else{
        return false;
     }
}

int main() {
    cin >> A;

    // Please write your code here.
    if(Modify(A)){
        cout<<"Yes"<<endl;
    }
    else{
      cout<<"No"<<endl;  
    }
    return 0;
}

