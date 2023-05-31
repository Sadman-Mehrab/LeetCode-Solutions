#include <bits/stdc++.h>
using namespace std;

class UndergroundSystem {
private:
    map<int,pair<int,string>> checkIns;
    map<pair<string,string>,vector<int>> times;
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        checkIns[id] = {t, stationName};
    }
    
    void checkOut(int id, string stationName, int t) {
        string prevStation = checkIns[id].second;
        int checkInTime = checkIns[id].first;
        times[{prevStation, stationName}].push_back(t - checkInTime);
    }
    
    double getAverageTime(string startStation, string endStation) {
        double sum = 0;
        vector<int> time = times[{startStation, endStation}];
        for(int x: time)
            sum += x;
        return (double)sum/time.size();
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */