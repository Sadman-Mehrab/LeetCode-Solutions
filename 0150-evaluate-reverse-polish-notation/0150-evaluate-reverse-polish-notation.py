class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t == '+' or t == '-' or t == '*' or t == '/':
                b, a = st[-1], st[-2]
                st.pop()
                st.pop()
                if t == '+':
                    st.append(a+b)
                elif t == '-':
                    st.append(a-b)
                elif t == '*':
                    st.append(a*b)
                elif t == '/':
                    st.append(int(a/b))
            else:
                st.append(int(t))
        return st[-1]