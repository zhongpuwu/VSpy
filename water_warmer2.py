import pandas as pd


def avg(L):
    sum = 0
    for i in L:
        sum += i
    return sum/24


environmental_temperature_summer = [26, 26, 25, 25, 24, 25, 26, 27, 29,
                                    30, 31, 31, 31, 32, 32, 32, 32, 31, 30, 29, 29, 28, 28, 27]  # 夏天室温观测值
environmental_temperature_winter = [
    6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]  # 冬天室温的观测值
l2 = []  # 存放最终结果
temperature_summer = avg(environmental_temperature_summer)  # 用于计算第二问的结果
temperature_winter = avg(environmental_temperature_winter)  # 用于计算第二问的结果
firstheat = 60  # 热水器的起始温度


def Radiation(T1, T2):  # 计算当前温度下的散热功率 第一个参数是当前温度 第二个参数是室温
    return 0.879*1.08*(T1-T2)


def OutV(T1, T2, T3):  # 第一个参数是当前温度 第二个参数是室温 第三个是需要的水温 获取当前时刻下热水阀放水的流量
    return 8*0.00001*60*4200*(T3-T2)/(60-T2)

T2 = temperature_winter  # 当前室温
l1 = [T2, 0]
time=0

while(l1[0]<60):
    Q=1500*1.0-Radiation(l1[0], T2)*1.0
    l1=[l1[0]+Q/(60*4200),l1[1]+Q]
    time+=1
print(time)

l1 = [60, 0]
flag = 0  # 加热判断
time = 0

for i in range(0, 900):  # 计算洗澡时的状态
    if(l1[0] <= 55):
        flag = 1
    if(l1[0] >= 60):
        flag = 0
    if(flag == 0):
        Q = 0-Radiation(l1[0], T2)*1.0+(T2-l1[0]) * \
            OutV(l1[0], T2, 42)/0.06  # 不加热时能量的变化
    if(flag == 1):
        Q = 0-Radiation(l1[0], T2)*1.0+(T2-l1[0]) * \
            OutV(l1[0], T2, 42)/0.06+1500*1.0  # 加热时能量的变化
        time += 1
    l1 = [l1[0]+Q/(60*4200), l1[1]+Q]
    l2.append(l1)
print(l1[0])
print(time)

l1[0]=55
time=0
while(l1[0]<=60):
    Q=1500*1.0-Radiation(l1[0], T2)*1.0
    l1=[l1[0]+Q/(60*4200),l1[1]+Q]
    time+=1
print(time)

l1[0]=60
time=0
while(l1[0]>=55):
    Q=-Radiation(l1[0], T2)*1.0
    l1=[l1[0]+Q/(60*4200),l1[1]+Q]
    time+=1
print(time)


# # 数据输出部分
# name = ['heaterTem', 'Power']
# test = pd.DataFrame(columns=name, data=l2)
# test.to_csv('D:/2/timely_heat2_winter.csv')
