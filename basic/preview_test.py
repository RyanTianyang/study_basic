# for i in range(1, 10):
#     print(i)
#
# str1 = "dfsgdfshjtsiugsadw"
# print(str1.split("s")[0])
#
'''不定长参数、字典做参数的使用'''
# dic = {
#
#     'dd': 123,
#     'fef': 67
# }
# li=('qq','aa','ww','ss')
# print(dic.get('asas', 88))
#
# def test(*args, **kwargs):
#     print(args)
#     print("------------")
#     print(kwargs)
# test(li,dic)
# test(*li,**dic)
# # test("ss","ww",vs="s",dw="w")
# test(11,(2,3,4),**{"sas":1,"dd":3})
#
#
#
# ar = (1, 2, 3, 4, 5)
# br = {'sas': 1, 'df': 4}
# test(ar, br)
# for x, y in br.items():
#     print(x, y)
#     #此处assert为断言，与下方判断用法一样
#     assert br[x] == y
#     if br[x] == y:
#         print("ok")
#     else:
#         print("no")
# hg = [1, 2, 3, 1]
# print(type(set(hg)))

# def hhas(greeting,city="beijing"):
#     return greeting,city
# print(hhas('dwdw',"dalian"))
# a=['s','d','f','e']
# b=['p','y','q','w']
# a.extend(b)
# print(a)
import logging

#
# logger = logging.getLogger('mylogger')
'''设置logger级别为debug能够打印所有级别日志，如果不设置默认只打印错误日志'''
# logger.setLevel(logging.DEBUG)

# fh = logging.FileHandler('test.log')
#
# formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
# fh.setFormatter(formatter)
# logger.addHandler(fh)
# logger.debug("goog goog")
# logger.info("hhhggggg")
# logger.error("nnneeeee")
# logger.info("ssasasqqq")
# with open('test.log') as hh:
#     print(hh.read())
# kk=open('test.log')
# aa=kk.read()
# print(aa)
# kk.close()
# try:
#     with open('sahsh.txt') as hh:
#         hh.read()
# except Exception as err:
#     print(str(err))
# a=['s','d','f','e']
# b=['p','y','q','w']
# c=zip(a,b)
# print(list(c))
# a=2.918
# print(int(a))
# print(bin(18))


# jj="Python is popular"
# jj.replace("Python","java")
# print(jj.replace("Python","java".upper()))
# kk=[1,2,3,4,5,6,7,8]
# ll=[]
# for x in kk:
#     if x%2==0:
#         ll.append(x)
# print(ll)
#
# person={"name":"tianyang",
#         "age":18,
#         "province":"黑龙江"}
# person["province"]="江苏"
# print(person)
#
#
# Test_str="Python was created in 1989, Python is using in AI, big data, IOT."
# ss=""
# for i in Test_str:
#     if i.isupper():
#         i=i.lower()
#     ss+=i
# print(ss)
#
# new_Test_str=Test_str.replace(",","")
# ssa=new_Test_str.split(" ")
# print(ssa)
#
# if len(ssa)%2==0:
#     pass
# else:
#     print(ssa[int(len(ssa)/2)])
#
# list1=["python", 5,6, 8]
# list2=["python","5", 6, 8,10]
# for x in list2:
#     list1.append(x)
# print(list1)
# print(set(list1))
# print(type("ss"))

# list1 = ["python", 5, 6, 8]
# list4=["sssas","ppooi112",1,25,2,3,4,5,44]
#
# def intp_lus(plus_list):
#     t = 0
#     for x in plus_list:
#         if "str" in str(type(x)):
#             pass
#         else:
#             t=t+x
#     return t
# print(intp_lus(list4))

# def defa(pp="ss",*args):
#     print(pp)
#     print(args)
#
# defa("sssa",1,1,2,3,45)
#
# '''默认参数与不定长参数和关键字参数的混合使用，
# 需要注意位置参数'''
# def test_canshu(aa="l",*args,**kwargs):
#     print(args)
#     print(aa)
#     print(kwargs)
#
# test_canshu(2,3,"kk", x = 4, y = 5, *[1, 2, 3], **{'a':1,'b': 2})
a=['aa','cc','vv','bb']
print(a[-1])