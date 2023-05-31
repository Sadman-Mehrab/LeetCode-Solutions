#include <bits/stdc++.h>
using namespace std;

class CustomStack {
private:
    int size = 0;

    vector<int> st;
public:
    CustomStack(int maxSize) {
        size = maxSize;
    }
    
    void push(int x) {
        if(st.size()<size){
            st.push_back(x);

        }
    }
    
    int pop() {
        if(st.size() == 0) return -1;
        else {
            int temp = st[st.size()-1];
            st.pop_back();
            return temp;
        }
    }
    
    void increment(int k, int val) {
        if(st.size() < k)
            for(int i=0;i<st.size();i++) st[i] += val;
        else{
            for(int i=0;i<k;i++) st[i] += val;
        }
    }
};
/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */