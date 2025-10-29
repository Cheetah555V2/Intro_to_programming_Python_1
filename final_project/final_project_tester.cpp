#include <iostream>
#include <cmath>
using namespace std;

bool sieve_of_eratosthenes_primitive_test(long long number, long long k) {
    if (number <= 2){
        return false;
    }

    long long s = 1;
    while ((number - 1) % (pow(2,s)) == 0) {
        s++;
    }
    s--;

    long long d = (number - 1) / (pow(2,s));

    for (long long i = 0; i < k; i++){
        
    }
}

int main(){
    if (sieve_of_eratosthenes_primitive_test(999999937)){
        cout << "Prime";
    }
    else{
        cout << "Not Prime";
    }

    return 0;
}