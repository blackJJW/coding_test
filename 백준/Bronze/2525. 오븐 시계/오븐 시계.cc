#include <iostream>

using namespace std;

int main() {
    int h, m;
    cin >> h >> m;
    
    int qm;
    cin >> qm;
    
    int cal_m = m + qm;
    
    if (cal_m < 60) {
        cout << h << " " << cal_m;
    } else {
        cout << (h + (cal_m / 60)) % 24 << " " << cal_m % 60;
    }
    
    return 0;
}