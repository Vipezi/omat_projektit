#include <iostream>
using namespace std;

int main(){
int number1;
char character = 'V';
string answer;
bool thisorthat;
double twoDecimals;
float numberWithComma;
cout << "Give me two numbers to substract: " << endl;
cin >> number1;
cin >> twoDecimals;
cout << "And one number to multiply them by: " << endl;
cin >> numberWithComma;
cout << "Your favourite letter is: ? " << (character)<< " ";
cin >> answer;
cout << "That is a good one!" << endl;
cout << "And the answer is: " << (number1 - twoDecimals) * numberWithComma  <<" " << endl;
cout << "Is this answer right? Answer true or false";
cin >> thisorthat;
cout << "Thank you for your time!"<< endl;
return 0;

}