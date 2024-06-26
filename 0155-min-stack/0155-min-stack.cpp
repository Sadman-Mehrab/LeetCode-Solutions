#include <bits/stdc++.h>
using namespace std;

class MinStack {
public:
    stack<int> st;
    stack<int> minStack;

    MinStack() {
       
    }
    
    void push(int val) {
        st.push(val);
        if(!minStack.empty()){
            if(val < minStack.top()) minStack.push(val);
            else minStack.push(minStack.top());
        }else{
            minStack.push(val);
        }
            
        
    }
    
    void pop() {
        st.pop();
        minStack.pop();
        
    }
    
    int top() {
        return st.top();
        
    }
    
    int getMin() {
        return minStack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */