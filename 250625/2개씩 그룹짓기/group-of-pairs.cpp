#include <iostream>
#include<algorithm> 

using namespace std;

int N;
int nums[2000];
int result[1000];

int main() {
    cin >> N;

    for (int i = 0; i < 2 * N; i++) {
        cin >> nums[i];
    }

    // Please write your code here.
    sort(nums,nums+(2*N));


    for (int i = 0; i < N; i++) {
        result[i] = nums[i] + nums[2*N-i-1];
        //cout <<nums[i]<<" + "<<nums[N-i]<<"= "<< result[i]<<endl;
    }

    sort(result,result+(N));

   cout << result[N-1];


    
    return 0;
}
