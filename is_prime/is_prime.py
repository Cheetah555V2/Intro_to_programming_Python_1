prime=int(input());flag=False
for i in range(2,int(prime**(1/2))):
    if prime%i==0:
        flag=True;break
print("Not Prime")if flag else print("Prime")