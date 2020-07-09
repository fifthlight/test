#列表里，pop有返回值，remove没有返回，pop加索引，remove加元素名
# list1=[1,1,1,2,2]
# print(list1.reverse())#这是打印的返回值
# print(list1)#这是打印的列表
#sorted直接返回排序后的列表，排序的规则按ascll码的排序
#元组可以在映射（或集合）中当作键使用
#循环多次的列表，不放在循环中修改，要新建一个新列表

#字典
#字典是有关系的
alien={'color':'green','points':5}
# print(alien['points'])#输入不存在的key值报错
# print(alien.get('points'))#不报错并且可以返回默认值，通过在后面加逗号加默认值
# alien['x_position']=10
# alien['y_position']=25
# print(alien)
# alien['y_position']=60
# print(alien)
# del alien['points']
# print(alien)

#遍历，items全都遍历。key只遍历key值，values只遍历value值
# for key,values in alien.items():
#     print(key,end='-')
#     print(values,end='/')
# for key in alien:
#     print(key)
for value in alien.values():#这个地方alien后面必须加values
    print(value)


