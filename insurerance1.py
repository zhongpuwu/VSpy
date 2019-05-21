import pandas as pd

def fan1(x):
    y1=500
    for i in range(80-x):
        if(i==60-x):
            y1+=200
        y1=(y1+4.5)*1.0505
    return y1+30

def fan2(x):
    y1=0
    for i in range(80-x):
        y1=(y1+6)*1.058
    return y1

l2=[]
for i in range(20,61):
    l=[i,fan1(i),fan2(i)]
    l2.append(l)

name=['FirstYearToPay','income1','income2']

test=pd.DataFrame(columns=name,data=l2)
test.to_csv('D:/1/FirstYearToPay_2.csv')