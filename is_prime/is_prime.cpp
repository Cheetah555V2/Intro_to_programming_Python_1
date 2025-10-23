#include <iostream>
#include <cmath>
using namespace std;

int main() {long long num;cin>>num;for(long long i=2;i<=sqrt(num);i++){if(num%i==0){cout<<"Not Prime";return 0;}}cout<<"Prime";return 0;}