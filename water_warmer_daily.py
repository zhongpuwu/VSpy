import pandas as pd


def avg(L):
    sum = 0
    for i in L:
        sum += i
    return sum/24


words = ['开始洗澡', '结束洗澡', '开始加热', '结束加热']
current = -1
environmental_temperature_summer = [26, 26, 25, 25, 24, 25, 26, 27, 29,
                                    30, 31, 31, 31, 32, 32, 32, 32, 31, 30, 29, 29, 28, 28, 27]  # 夏天室温观测值
environmental_temperature_winter = [
    6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]  # 冬天室温的观测值
l2 = []  # 存放最终结果
l = []  # 存放每一对开始结束时间
temperature_summer = avg(environmental_temperature_summer)  # 用于计算第二问的结果
temperature_winter = avg(environmental_temperature_winter)  # 用于计算第二问的结果
top_heat = 45
bottom_heat = top_heat-5


def Radiation(T1, T2):  # 计算当前温度下的散热功率 第一个参数是当前温度 第二个参数是室温
    return 0.879*1.08*(T1-T2)


def OutV(T1, T2, T3):  # 第一个参数是当前温度 第二个参数是室温 第三个是需要的水温 获取当前时刻下热水阀放水的流量
    return 8*0.00001*60*4200*(T3-T2)/(60-T2)


T2 = temperature_summer  # 当前室温
l1 = [T2, 0]  # 起始温度是当前室温
time = 0
flag = -1  # 状态变化周期 分为4个状态 最后一种是无状态
flags = 0  # 是否在洗澡
w_timer = 0  # 洗澡时间的倒计时

for i in range(0, 24*60*60*7+1):#用m和current确定转折点
    Q = -Radiation(l1[0], T2)*1.0  # 日常散热
    l1 = [l1[0]+Q/(60*4200), 0]
    if(i % (24*60*60) == 0):
        current=-1
        flag = 0
        if(len(l) == 0):
            l.append(i)
        elif(len(l) == 2):
            l2.append(l)
            print(l[1]-l[0])
            l = []
            l.append(i)
        print('开始加热')
    if(l1[0] > top_heat):
        m=0
        if(m!=current):
            current=0
            flag = 1
            flags = 1
            w_timer = 900
            if(len(l) == 1):
                l.append(i)
            print('结束加热')
    if(l1[0] < bottom_heat and flags==1):
        m=1
        if(m!=current):
            current=1
            flag = 2
            print('开始加热1')
            if(len(l) == 0):
                l.append(i)
            elif(len(l) == 2):
                l2.append(l)
                l = []
                l.append(i)   
    if(w_timer < 2 and flags==1):
        m=2
        if(m!=current):
            current=2
            flags=0
            flag = 3
            if(len(l) == 1):
                l.append(i)
            print('结束洗澡')
    # 下面是具体动作
    if(flag == 0):
        Q = 1500*1.0
        l1 = [l1[0]+Q/(60*4200), 0]
        time += 1
    elif(flag == 1):
        Q = -(l1[0]-T2)*OutV(l1[0], T2, 37)/0.06
        l1 = [l1[0]+Q/(60*4200), 0]
        w_timer -= 1
    elif(flag == 2):
        Q = -(l1[0]-T2)*OutV(l1[0], T2, 37)/0.06+1500*1.0
        l1 = [l1[0]+Q/(60*4200), 0]
        w_timer -= 1
        time += 1

print(l2)
print(time)

# 输出最终结果
name = ['start_times', 'stop_times']
test = pd.DataFrame(columns=name, data=l2)
test.to_csv('D:/2/timely_summer_daily.csv')