import pandas as pd


def avg(L):
    sum = 0
    for i in L:
        sum += i
    return sum/24


words = ['开始洗澡', '结束洗澡', '开始加热', '结束加热']
TimerUsing=[]

environmental_temperature_summer = [26, 26, 25, 25, 24, 25, 26, 27, 29,
                                    30, 31, 31, 31, 32, 32, 32, 32, 31, 30, 29, 29, 28, 28, 27]  # 夏天室温观测值
environmental_temperature_winter = [
    6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]  # 冬天室温的观测值

temperature_summer = avg(environmental_temperature_summer)  # 用于计算第二问的结果
print(avg(environmental_temperature_summer))
temperature_winter = avg(environmental_temperature_winter)  # 用于计算第二问的结果
print(avg(environmental_temperature_winter))



def Radiation(T1, T2):  # 计算当前温度下的散热功率 第一个参数是当前温度 第二个参数是室温
    return 0.879*1.08*(T1-T2)


def OutV(T1, T2, T3):  # 第一个参数是当前温度 第二个参数是室温 第三个是需要的水温 获取当前时刻下热水阀放水的流量
    return 8*0.00001*60*4200*(T3-T2)/(60-T2)

def GetTime(a):
    l2 = []  # 存放最终结果
    l = []  # 存放每一对开始结束时间
    current = -1
    top_heat = a
    bottom_heat = top_heat-5
    T2 = temperature_winter  # 当前室温
    l1 = [top_heat, 0]
    time = 0
    flags = 0  # 是否在洗澡
    flag = 0  # 是否在加热
    w_timer = 0  # 洗澡时间的倒计时

    for i in range(0, 24*60*60*7):
        if(i % (24*60*60) == 0):
            flags = 1
            w_timer = 900
        elif(w_timer < 2):
            flags = 0
        if(l1[0] < bottom_heat):  # 记录开始加热的时机
            flag = 1
            m = 2
            if(m != current):
                if(len(l) == 0):
                    l.append(i)
                elif(len(l) == 2):
                    l2.append(l)
                    l = []
                    l.append(i)
                current = 2
        if(l1[0] > top_heat):
            flag = 0
            m = 3
            if(m != current):
                if(len(l) == 1):
                    l.append(i)
                current = 3
        Q = -Radiation(l1[0], T2)*1.0
        l1 = [l1[0]+Q/(60*4200), 0]
        if(flags == 1):
            Q = -(l1[0]-T2)*OutV(l1[0], T2, 42)/0.06
            l1 = [l1[0]+Q/(60*4200), 0]
            w_timer -= 1
        if(flag == 1):
            Q = 1500*1.0
            l1 = [l1[0]+Q/(60*4200), 0]
            time += 1    
    return time
for i in range(49+5,76):
    TimerUsing.append([i,GetTime(i)])
    print(GetTime(i))
print(TimerUsing)

# 输出最终结果
name = ['Setting','TimeUsing']
test = pd.DataFrame(columns=name, data=TimerUsing)
test.to_csv('D:/2/timeUsing_winter.csv')
