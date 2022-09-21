#include <iostream> // Made for comments
using namespace std;

int main(){
    float number1 = 5;
    int number2 = 5;
    float number3;
    string myText = "bus";
    int sum = number1 + number2;
    cout << "Input a number integer: ";
    cin >> number3;
    // cout << "This is the sum of number1 and number2: " << sum <<endl;
    cout << "Sum of sum and number3 is: " << number3 + sum << endl;
    cout << "Which vehicle can move multiple passengers: " << myText << endl;
    return 0;
}