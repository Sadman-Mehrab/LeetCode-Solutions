class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t == '+':
                a = st[-1]
                st.pop()        
                b = st[-1]
                st.pop()        
                st.append(b+a)
            elif t == '-':
                a = st[-1]
                st.pop()        
                b = st[-1]
                st.pop()        
                st.append(b-a)
            elif t == '*':
                a = st[-1]
                st.pop()        
                b = st[-1]
                st.pop()        
                st.append(b*a)
            elif t == '/':
                a = st[-1]
                st.pop()        
                b = st[-1]
                st.pop()        
                st.append(int(b/a))
            else:
                st.append(int(t))
        
        return st[-1]
            

