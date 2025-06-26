#include <iostream>
#include <string>
#include<algorithm>

using namespace std;

string word1;
string word2;
bool flag = true;

int main() {
    cin >> word1;
    cin >> word2;

    // Please write your code here.
    sort(word1.begin(),word1.end());
    sort(word2.begin(),word2.end());
    
    if(word1.size() != word2.size())
        flag = false;
    else{

        for(int i = 0; i < word1.size(); i++)
        {
            if(word1[i] != word2[i])
            {
                flag = false;
                break;
            }
        }

    }
    

    if(flag ==true)
        cout<< "Yes";
    else
        cout<< "No";
    return 0;
}
