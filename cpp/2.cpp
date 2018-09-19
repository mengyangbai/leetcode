#include <iostream>

using namespace std;

double calcPay(double workhour, double rate){
    double result = workhour * rate;
    if(workhour > 40.0){
        result += (workhour - 40.0) * rate * 0.5;
    }
    return result;
}

int main()
{
    cout<<calcPay(41,10);
    return 0;
}
