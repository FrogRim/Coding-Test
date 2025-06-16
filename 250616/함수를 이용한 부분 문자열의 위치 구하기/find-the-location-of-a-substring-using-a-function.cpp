#include <iostream>
#include <string>
#include<algorithm>


using namespace std;

string text;
string pattern;

int main() {
    cin >> text;
    cin >> pattern;

    // Please write your code here.
    if(text.find(pattern) != std::string::npos){
        cout << text.find(pattern) << endl;

    }
    else{
        cout << "-1" << endl;
    }

    return 0;
}