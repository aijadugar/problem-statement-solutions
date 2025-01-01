from collections import deque

st = deque()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

for tkn in tokens:
    if tkn == '+':
        st.append(st.pop() + st.pop())
    elif tkn == '-':
        t1 = st.pop()
        t2 = st.pop()
        st.append(t2 - t1)
    elif tkn == '*':
        st.append(st.pop() * st.pop())
    elif tkn == '/':
        t1 = st.pop()
        t2 = st.pop()
        st.append(int(t2/t1))
    else:
        st.append(int(tkn))
        
print(st[-1])
    
        

