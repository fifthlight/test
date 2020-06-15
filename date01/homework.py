#第一个大问题，list去重
#1、
# #利用集合内元素无法重复来去重
# list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
#
# list2=list(set(list1))
# print(list2)

#2、
#通过循环遍历去掉重复项再写入
# list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
# list2=[]
# for i in list1:
#     if i not in list2 :
#         list2.append(i)
# print(list2)

# #上述方法可以简写
# list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
# list2=[]
# [list2.append(i) for i in list1 if i not in list2]
# print(list2)

#3、
# #这是啥方法？转化字典？据说这种速度快
# list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
# list2=list({}.fromkeys(list1).keys())
# print(list2)

#4、
#这种用list内的sort方法，这个方式可以保持列表的顺序不变
# list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
# #这里也可以写成
# # list2=list(set(list1))
# # list2.sort(key=list1.index)
# list2=sorted(set(list1),key=list1.index)
# print(list2)

'''
其中字典和集合两种方法会改变顺序，其他可以保持顺序
'''

#5、这种不知道为什么不好用
#这种方式不是缺参数，就是无定义
# #list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
# # list.sort(list1)
# # list2=[]
# # for i in range(len(list)-1):
# #     if list[i]==list[i+1]:
# #         list2.append(list[i+1])
# #         for j in list2:
# #             list.remove(j)
# # print(list2)
#
# list.sort()
# del_lst = []
# for i in range(len(list) - 1):
#     if list[i] == list[i + 1]:
#         del_lst.append(list[i + 1])
# for j in del_lst:
#     list.remove(j)

#6、
# list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
# list2=[]
##fromkeys是对所有的键赋同样的值，如果不指定内容则默认赋值为none
# dct=dict.fromkeys(list1)
# print(dct)
# for n in dct:
#     list2.append(n)
# print(list2)

# #也可以简写
# list1=[1,2,5,6,7,4,8,2,7,9,4,6,3]
# print(list(dict.fromkeys(list1)))


#第二个问题，编写数字与月份对应
# str1=input('请在1，2，3，4中，选择一个你心仪的一个数字输入')
# if str1=='1':
#     print('正月')
# elif str1=='2':
#     print('二月')
# elif str1=='3':
#     print('三月')
# elif str1=='4':
#     print('四月')
# else:
#     print('你能不能按套路来')

#将月份与数字调换


#
# str_x=input('选择一个你喜欢的月份输入吧,例如一月，二月，三月等')
# if str_x=='一月'or'十一月':
#     print('你可能和水有莫名的缘分吧')
# elif str_x=='二月'or'三月'or'五月':
#     print('你是不是总有好多好多精力哇')
# elif str_x=='四月'or'六月'or'七月'or'九月':
#     print('你可能会喜欢热烈美好的生活吧')
# else:
#     print('如果世上真的有奇迹，那只是努力的另一个名字')

#第三个问题，猜价格
#   q=input('猜猜神秘商品的价格吧')
#   p='188.5'
#
# if q>p :
#     print('没有这么贵吧')
# elif q<p:
#     print('你这也太便宜了')
# else:
#     print('这都被你猜到了')

# #这种你有五次机会不猜对不停止
# for i in range(5):
#     q = input('输入一个你认为可能的价格')
#     p ='188.5'
#     if (q==p):
#         print('这都被你猜到了')
#         break
#     elif q<p :
#         print('别太便宜呀')
#         print('您还有%d次机会' %(4-i))
#     elif q>p :
#         print('这有点贵')
#         print('您还有%d次机会' % (4 - i))
#
# else:
#     print('失败超过5次，请稍后再试')

#第四个问题，变量从创建、引用到最后销毁的过程
'''
1、当变量赋值之后，就根据赋值类型被相应创建了
2、只要被引用一次，计数器就会自增1
其中传值内存地址不变，例如字母数字；
而传引用内存地址改变，例如列表，字典。
3、销毁有这么几种方式
（1）一个本地引用离开了其作用范围
（2）别名被显式销毁，引用计数值为0，等待垃圾回收，如del x
（3）对象的一个别名被赋值给另一个对象
（4）对象被从一个窗口对象中移除 例如 mylist.remove(x)
（5)窗口对象本身被销毁
'''