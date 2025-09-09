def isBalanced(str):
    st = []
    mapp = {'}':'{' , ')' : '(' , ']' : '['}
    for i in str:
        if i in mapp.values():
            st.append(i)
        
        elif i in mapp.keys():
            if not st or mapp[i]!=st.pop():
                return 'No'

    return 'Yes' if not st else 'No'

stri = '({[]})'
print(isBalanced(stri))