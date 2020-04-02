'''
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
处理:
1.记录最多8条错误记录，对相同的错误记录(即文件名称和行号完全匹配)只记录一条，错误计数增加；(文件所在的目录不同，文件名和行号相同也要合并)
2.超过16个字符的文件名称，只记录文件的最后有效16个字符；(如果文件名不同，而只是文件名的后16个字符和行号相同，也不要合并)
3.输入的文件可能带路径，记录文件名称不能带路径

输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

    文件路径为windows格式

    如：E:\V1R2\product\fpgadrive.c 1325


输出描述:
将所有的记录统计并将结果输出，格式：文件名代码行数数目，一个空格隔开，如: fpgadrive.c 1325 1 

    结果根据数目从多到少排序，数目相同的情况下，按照输入第一次出现顺序排序。

    如果超过8条记录，则只输出前8条记录.

    如果文件名的长度超过16个字符，则只输出后16个字符
示例1
输入
E:\V1R2\product\fpgadrive.c 1325
输出
fpgadrive.c 1325 1
'''
'''
其实可以用os.path.split()分隔出文件名，但是牛客网不支持
'''
record = {}   #创建字典存放文件
lis = []
index = 0
while True:
    try:
        file = list(input().strip().split('\\'))   #分隔\要用'\\'(注意是两个斜杠)
        fullname = file[-1]
        P = fullname.split(' ')
        fname, frow = P[0], P[1]
        if fullname not in record:
            record[fullname] = []
            if len(fname) > 16:
                fname = fname[-16:]
            record[fullname] = [fname, frow, 1, index]   #index存放输入的先后顺序
            index += 1
        else:
            record[fullname][2] += 1
    except:
        break

for t in record:   
    lis.append(record[t])  #把字典中的list存到lis中，注意这里的用法
final_lis = sorted(lis, key=lambda k:(-k[2], k[3]))   #对lis进行排序
if index > 8:
    for j in range(8):
        print(final_lis[j][0], end=' ')
        print(final_lis[j][1], end=' ')
        print(final_lis[j][2])
else:
    for j in final_lis:
        print(j[0], end=' ')
        print(j[1], end=' ')
        print(j[2])

