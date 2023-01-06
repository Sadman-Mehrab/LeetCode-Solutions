class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for(char x: s)
            if(x == ')' || x == '}' || x == ']')
                if(st.empty()) return false;
                else if(x == ')' && st.top() != '(') return false;
                else if(x == '}' && st.top() != '{') return false;
                else if(x == ']' && st.top() != '[') return false;
                else st.pop();
            else st.push(x);
        return st.empty() ? true : false;
    }
};