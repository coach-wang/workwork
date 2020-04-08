#输入单个数字：
a = int(input().strip())
#输入单个字符串并转化为list：
b = list(input().strip())
#输入多个list
P = []
for i in range(n):
    P.append(list(map(int, input().strip().split())))
#创建字典：
dic = {}
idea = list()
if idea[i] not in dic:
    
    dic[idea[i]].append(idea)
#读取字典：
for t in dic:   
    lis.append(dic[t])  #把字典中的list存到lis中，注意这里的用法
final_lis = sorted(lis, key=lambda k:(-k[2], k[3]))   #对lis进行排序
#如果不确定输入的数量，使用：
while True:
    try:
    except:
        break
