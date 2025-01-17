#include <iostream>

using namespace std;

int main() {
    int h, m;
    cin >> h >> m;
    
    int caled_m = m - 45;
    
    if (caled_m >= 0) {
        cout << h << " " << caled_m;
    } else {
        if (h - 1 < 0) {
            cout << 24 + h - 1 << " " << 60 + caled_m;    
        } else {
            cout << h - 1 << " " << 60 + caled_m;    
        }
    }
    
    return 0;
}