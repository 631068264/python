# coding=utf-8
# __author__ = 'wuyuxi'
import datetime

print("Hello world")

print "flalflajf aljfla;f 46464646"

print "464", "4546f4645f46a"  # 字符串拼接

print '200 + 100 = ', 100 + 200

# name = raw_input('输入你的名字 ')  # 控制台输入
# print 'hello', name

is_ok = False
if not is_ok:
    print(is_ok)

message = {"create_time": datetime.datetime.now()}


def lala():
    message["age"] = 12
    message["hello"] = 45
    print(message)


lala()


class stu(object):
    pass


s = stu()
s.age = 12
s.team = 65
print(s)

list1 = [1, 5, 6, 8]
l = [1, 5, 6, 8, 9, 4, 6, 4, 2, 7, 6, 6]

# l = [l2 for l2 in l if l2 not in list1]  # 删除相同元素
l.append(list1)
print(l)
