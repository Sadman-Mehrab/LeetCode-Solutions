#include <bits/stdc++.h>
using namespace std;

class ParkingSystem {
private:
    int big = 0, medium = 0, small = 0;
    int bigCap = 0, mediumCap = 0, smallCap = 0;
public:
    ParkingSystem(int big, int medium, int small) {
        bigCap = big;
        mediumCap = medium;
        smallCap = small;
    }
    
    bool addCar(int carType) {
        if(carType == 1){
            if(big + 1 <= bigCap){
                big++;
                return true;
            }
            else return false;
        }
        else if(carType == 2){
            if(medium + 1 <= mediumCap){
                medium++;
                return true;
            }
            else return false;
        }
        else if(carType == 3){
            if(small + 1 <= smallCap){
                small++;
                return true;
            }
            else return false;
        }
        return false;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */