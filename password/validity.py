l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
if (len(s) >= 8):
    for i in s:
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        if (i.isdigit()):
            d+=1
        if(i=='@'or i=='$' or i=='_'):
            p+=1
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("Valid Password")
else:
    print("Invalid Password")