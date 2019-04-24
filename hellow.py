import random
a=0
b=0
c=0
d=0
e=0
for i in range(1,50):
    r=random.randint(1,50)
    if(r<=10):
        a+=1 
    elif(r<=20):
        b+=1
    elif(r<=30):
        c+=1
    elif(r<=40):
        d+=1
    else:e+=1
print(a)
print(b)
print(c)
print(d)
print(e)
