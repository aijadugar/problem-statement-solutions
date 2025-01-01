from collections import deque

st = deque()

path = "/../"

new_path = path.split('/')

if path == "/../":
    print("/")
for pt in new_path:
    if pt == '.':
        continue
    elif st and pt == '..':
        st.pop()
    else:
        st.append(pt)

new_st = deque(['/' + ele for ele in st])

ans = ''.join(new_st)


while '//' in ans:
    ans = ans.replace('//', '/')

print(ans.rstrip('/'))