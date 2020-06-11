# import math
# r=10
# S=math.pi*r**2
# L=2*math.pi*r
# S2=math.pi*pow(r,2)
# print(S,S2,L)
# year=2019
# if(year % 4 == 0 and year%100!=0) or (year%400==0):
#     print("闰年")

#定义用户输入，定义一个输入接口。并用int将用户输入转化为整数型
# year=int(input("请输入要查询的年份："))
# #创建两个判断条件，用于判断输入是否是闰年
# term1=(year%4==0 and year%100!=0)
# term2=(year%400==0)
# #使用流程控制打印对应提示
# if(term1 or term2):
#     print("您好",year,"是闰年")
# else:
#     print(year,"是平年")
# import math
# r=float(input("请输入半径"))
# S=math.pi*pow(r,2)
# L=2*math.pi*r
# print(S,L)
# import calendar
# year=int(input("请输入要查询的年份"))
#
# (calendar.isleap(year))
# if(True):
#     print(year,"是闰年")
# else:
#     print(year,"是平年")
# y=int(input("输入年份"))
# result=(y%4==0 and y%100!=0 or y%400==0)
# print(result)

# from sys import getrefcount
# a = [1, 2, 3]
# print(getrefcount(a))
# b=a
# c = [a, a]
# print(getrefcount(a))
# del c,b
# print(getrefcount(a))
# del a
# print("a被销毁了")

#选择分支语句
# str_num=input("大家今天早上想吃什么，输入1，2，3,将随机选择")
#
# # print(str_num)
# #注意有引号没引号是区分字符串与其他的数据类型进行区分
# if str_num=='1' :
#     print("包子")
# elif str_num=='2':
#     print("豆浆油条")
# elif str_num=='3':
#     print("面包香肠")
# else:
#     print("别吃了")

