'''a="vinoth"   
b=1111
c=100000
d="varun"
e=2222
f=200000
g="surya"
h=3333
i=300000
j="pavin"
k=4444
l=400000
m="kavin"
n=5555
o=500000
ae=[]



    
for y in range(0,5):
    
    
    p=input("Enter your Name:")
    ae.append(p)
    q=int(input("Enter your PIN:"))
    r=int(input("1.Deposit,2.Withdraw"))
    ae.append(r)
    s=int(input("Enter your amount:"))
    ae.append(s)
    if p==a and q==b and r==1:
        print("Please deposit your cash")
        t=c+s
        ae.append(t)
        c=t
        ae.append(c)
        print("Your account balance is:",t)
        print(ae)
    elif p==a and q==b and r==2:
        print("Please collect your cash")
        t=c-s
        ae.append(t)
        c=t
        ae.append(c)
        print("Your account balance is:",t)
        print(ae)
    elif p==d and q==e and r==1:
        print("Please deposit your cash")
        u=f+s
        ae.append(u)
        f=u
        ae.append(f)
        print("Your account balance is:",u)
    elif p==d and q==e and r==2:
        print("Please collect your cash")
        u=f-s
        ae.append(u)
        f=u
        ae.append(f)
        print("Your account balance is:",u)
    elif p==g and q==h and r==1:
        print("Please deposit your cash")
        v=i+s
        ae.append(v)
        i=v
        ae.append(i)
        print("Your account balance is:",v)
    elif p==g and q==h and r==2:
        print("Please collect your cash")
        v=i-s
        ae.append(v)
        i=v
        ae.append(i)
        print("Your account balance is:",v)
    elif p==j and q==k and r==1:
        print("Please deposit your cash")
        w=l+s
        ae.append(w)
        l=w
        ae.append(l)
        print("Your account balance is:",w)
    elif p==j and q==k and r==2:
        print("Please collect your cash")
        w=l-s
        ae.append(w)
        l=w
        ae.append(l)
        print("Your account balance is:",w)
    elif p==m and q==n and r==1:
        print("Please deposit your cash")
        x=o+s
        ae.append(x)
        o=x
        ae.append(o)
        print("Your account balance is:",x)
    elif p==m and q==n and r==2:
        print("Please collect your cash")
        x=o-s
        ae.append(x)
        o=x
        ae.append(o)
        print("Your account balance is:",x)
    else:
        print("Please enter correct details")'''






