


number=int(input('请您告诉我您一共有几个人同行呢'))
for i in range(number):
    age=int(input('请出示您的年龄证明'))
    if age<4:
        print('可以免费哦')
    if 4<=age<18 or age>65:
        print('您只需付五美元即可')
    if age>125:
        print('我们这里好像是普通人类的售票处，旁边是特殊售票点')
    else:
        print('您需要支付10美元')
# import random
# c1='green'
# c2='yellow'
# c3='red'
# alien_color=random.choice(c1,c2,c3)
# print(alien_color)
# if alien_color == 'green':
#     print('you get 5 points')
# else:
#     print('you have turned on hidden rewards,get 10 points')


















