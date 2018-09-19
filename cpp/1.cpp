#include <iostream>

using namespace std;

void numberSign(int num){
    if(num == 0){
        std:cout<<"zero";
    }
    else if(num > 0){
        std:cout<<"positive";
    }
    else{
        std:cout<<"negative";
    }
}

int main()
{
    numberSign(4);
    numberSign(-4);
    numberSign(0);
}