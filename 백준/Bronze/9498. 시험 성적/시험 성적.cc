#include <iostream>

using namespace std;

int main() {
    int score;
    cin >> score;
    
    if (score > 89 && score <= 100) {
        cout << "A";
    } else if (score > 79 && score <= 89) {
        cout << "B";
    } else if (score > 69 && score <= 79) {
        cout << "C";
    } else if (score > 59 && score <= 69) {
        cout << "D";
    } else {
        cout << "F";
    }
    
    return 0;
}