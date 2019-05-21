import pandas as pd

l2=[]
y1=0
y2=0

for i in range(50,81):
    y1=(y1+4.5)*1.0505
    y2=(y2+6)*1.058
    l=[i,y1*0.0505/1.0505,y2*0.058/1.058]
    l2.append(l)

name=['Year','YearlyIncome1','YearlyIncome2']

test=pd.DataFrame(columns=name,data=l2)
test.to_csv('D:/1/YearlyIncome50.csv')