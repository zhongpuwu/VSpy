def avg(L):
    sum = 0
    for i in L:
        sum += i
    return sum/24

def Radiation(T1, T2):  # 计算当前温度下的散热功率 第一个参数是当前温度 第二个参数是室温
    return 0.879*1.08*(T1-T2)

environmental_temperature_summer = [26, 26, 25, 25, 24, 25, 26, 27, 29,
                                    30, 31, 31, 31, 32, 32, 32, 32, 31, 30, 29, 29, 28, 28, 27]  # 夏天室温观测值
environmental_temperature_winter = [
    6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4]  # 冬天室温的观测值
l2 = []  # 存放最终结果
temperature_summer = avg(environmental_temperature_summer)  # 用于计算第二问的结果
temperature_winter = avg(environmental_temperature_winter)  # 用于计算第二问的结果
top_heat=60
bottom_heat=top_heat-5

l1 = [20, 0]
time=0
T2=temperature_winter
while(l1[0] <= top_heat):
    Q=1500*1.0-Radiation(l1[0], T2)*1.0
    l1=[l1[0]+Q/(60*4200),l1[1]+Q]
    time+=1
print(time)