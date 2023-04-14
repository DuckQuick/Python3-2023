"""
2023-4-14 16:09:28
问题:600个人站一排,每次随机杀掉一个奇数位的人,几号最安全
"""
import random

def num1(length):
    return [x for x in range(1,length + 1)]
    
num = 10000
length = 600
arr = [0 for i in range(num)]

for n in range(num):
    a = num1(length)
    for i in range(length - 1):
        del a[random.randrange(0,length - i,2)]
    arr[n] = a[0]
    
for i in range(1,length + 1):
    print(f"数字{i}存活的次数: {arr.count(i)} ,占比:{arr.count(i) / length}")
