#建立接口
c=input("请输入一个字符或ascll码")
#用户输入ascll码，并将其转化为整型
a=int(input("请输入一个ascll码"))
#这里的c是字符串，故可以加
print(c,"的ascll码是",ord(c))
#这里不能用加号，因为a转了形式，现在的a是整型，而数字型不能够和字符串相加，所以这里要用逗号
print(a,"的字符是",chr(a))
