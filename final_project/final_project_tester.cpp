#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

bool sieve_of_eratosthenes_primitive_test(long long number) {
    vector<bool> sieve(number + 1, true);

    for (int i = 0; i <= number; i++) {
        sieve[i] = true;
    }

    sieve[0] = false;
    sieve[1] = false;

    long long limit = sqrt(number);

    for (long long index = 2; index <= limit; index++) {
        if (sieve[index]) {
            for (int multiple = index * index; multiple <= number; multiple += index) {
                sieve[multiple] = false;
            }
        }
    }

    return sieve[number];
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