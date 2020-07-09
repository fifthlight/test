
#books = ["lanuage", ["python", "java"], "name", ["tom ","sophoie"],88]
# for book in books:
#     if isinstance(book,list):
#         for item in book:
#             print(item)
#     else:
#         print(book)

# books.pop(-2)
# print(books)

# names=[ 'soph','Rain','Jack','linda','tom','tom','Black']
# names.insert(-1,'Blue')
# print(names)
# names.remove('soph')
#
# names.insert(0,'索菲')
# print(names)
# names.insert(2,["oldboy","oldgirl"])
# print(names)
#
# print(list(enumerate(names)))
# print(names.index('tom'))#这种写法简单，但是缺点是他无法找重复单位

#这种方法可以找重复单位
# for i,x in enumerate(names):
#     if x=='tom':
#         print(i)
# print([i for i,x in enumerate(names) if x=='tom'])#这种写起来更简便
list1=[1,2,3,4,2,5,6,2,]
# names.extend(list1)
# print(names)
# # names[0:0]=list1
# # print(names)
# names[1:2]=list1
# print(names)
# print(list1[4:8])
# print(list1[2:11:2])
# print(list1[-3::])
for i,x in enumerate(list1):

    if i%2==0:
        list1[index]=-1
        




