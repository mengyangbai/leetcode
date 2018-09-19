#include <iostream>

using namespace std;

int isLeapYear(int year){
    if(year%4==0){
        if(year%100==0){
            if(year %400==0){
                return 1;
            }
            return 0;
        }
        return 1;
    }
    return 0;
}

int main()
{
    cout<<isLeapYear(2001);

    return 0;
}
