
# int1=11212
# s=repr(int1)
# ss=str(int1)
# print(s,ss)

#不可变对象是不能在原有的上面改变，只能复制一个又改变
#不可变对象就是查询和排序
#可变对象，增删改查，也是对数据的基本操作

#数字求长度len,0b代表二进制
# x=10
# b=x.bit_length()
# print(b)

#字符串
# str1='abcdef'
#索引，从前往后就是从0 开始，从后往前，从-1开始
#切片
#start:end:step
# print(str1[1:])
# print(str1[:-2])
# print(str1[-1:])
# print(str1[2:4])
# print(str1[::2])
# print(str1[::-1])#倒序输入
# print(str1[::1])
# print(str1[:2])#取前两位
# print(str1[::])#显示所有字符

#遍历
# for char in str1:
#     print(char+'疯了',end="")#这是一个一个输出，一个一个的给char
#   #  print(char)
#     #加了一个end=''就不会一个一个的形式，但其实本质还是没变，只是去掉空格

# str2='c:\nfj\dfj\fdf.txt'
# str3='c:\nfj\d\tfj\fdf.txt'
# str22=r'c:\nfj\dfj\fdf.\'txt'
# str2__='c:\\nfj\dfj\\fdf.txt'
# str2_=r'c:\nfj\dfj\fdf.txt'
# print(str2,str2_,str2__,str22,str3)

# str1='0123456789'
# print(str1[::2])
# print(str1[::-1])
# str1="{\"name\":\"fifth\"}"
# print(str1)

#[]的意思是可有可无
#查找，index，find
# str1="{\"name\":\"fifth\"}"
# print(str1)
# print(str1.index('n',2))
# print(str1.index('name',2,5))
#
# print(str1.find('n'))
# print(str1.find('o'))
# print(str1.index('0'))#index找不到报异常，find返回-1，注意计算机只要执行到异常，就不再往下进行
# print(str1.count('n'))#count 出现了几次
# print(str1.rfind('name',1))#虽然是从右找，但是还得从0找
# print(min(str1))
# print(max(str1))
# print(len(str1))

#替换replace
# str4='多情剑客无情剑'
# # str5='you are a cat'
# # print(str4.replace('剑','刀',1))
# # print(str4.replace('剑','刀',2))
# # print(str5.split('no',2))
# print('才'.join(str4))
# print('剑'.join(str4))
# print(str4.join('才才'))
#
#
# path = 'hive://ads/training_table'
# print(path[7:10])
# print(path[11:])
# print(path.split('/',3))
# n=path.split('/training_table')
# m=str(n)
# k=m.split('hive://')
# print(k)


# str1='pythonconfidence'
# print(str1.replace('python','java'))
# print(str1.upper()[1:3])
# print(str1.split('y')[1].split('h')[1])
# #因为字符串是不可变的，所以要往里插东西，先转成列表
# list1=list(str1)
# list1.insert(6,'is')
# #想在哪插就写哪的索引
# list1.insert(6,' ')
# list1.insert(8,' ')
# l=str(list1)
# print(l)
# print(''.join(list1))#这句可以让列表转回字符串并成句

import difflib
str4='Youthe star, youthe moon, youunspeakable once'
list2=list(str4)
list2.insert(3,' are ')
print(''.join(list2))
seq = ("l", "i", "n", "d", "a")
print(''.join(seq))

