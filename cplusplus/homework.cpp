#include <iostream>
using namespace std;


// The first task
int first(){
    int num = 10;
    int num2 = 3;
    cout << num + num2;
    return 0;
}

// The second task
int second(){
    string name {};
    cout << "Please tell me your name: " << endl;
    getline(cin, name);
    cout << name << endl;
    return 0;
}

// The third task
int third(){
    string address{};
    string name{};
    cout << "Give me your name: ";
    getline(cin, name);
    cout << "Give me your address: ";
    getline(cin, address);
    cout << name << " Lives in the address: " << address;
    return 0;
}

int main(){
    first();
    second();
    third();
}