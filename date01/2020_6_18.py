# str1='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv'
# print(str1.strip('v'))

# str3='我说:我今天很高兴'
# str4='编号 标题 测试数据 测试结果'
# print(' '.join(str4))
# print(str3.split(':')[1].split('我'))
# str3.split(':')[1].split('我')
# print(''.join(str3))

#没写完
# import time
# str2='hello'
# str2='H'+str2[1:]
# print(str2)
# time.perf_counter()

#列表
# book=['you',['sad'],'no',['shout']]
# for i in book:
#     if isinstance(i,list):
#         for i1 in i:
#             print(i1)
#     else:
#         print(i)


name=['white','linda','black','jony','july']
name.insert(2,'blue')#插入到索引2的前面
print(name)
name.remove('jony',)
name.insert(-1,'朱莉')
print(name)

#enumerate可以打印索引

