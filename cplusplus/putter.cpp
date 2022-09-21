#include <iostream>
using namespace std;

int main(){
    string name {};
    cout << "Write your full name ";
    // cin >> name;
    getline(cin, name);
    cout << name;
}