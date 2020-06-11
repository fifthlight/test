# list1=[1,2,2]
# #list定义一定要用中括号【】，如果用括号（）会被认定为元组
# list1.append (2)
# print(list1)
# list2=("abc",3,4)
#
# list3=list1+list2
#
# print(list1+list2)
# print(id(list1),id(list2),id(list3))
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [list1 + list2]

my_info = ()
dic1 = {'name': '李安', 'age': '18'}
#注意这里print外面小括号里面中括号
print(dic1 ['name'])
print(dic1['age'])

