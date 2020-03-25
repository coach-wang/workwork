'''
小明是一个数学家，他喜欢用数字给事物命名编号，他给自己编号为1，同时在2019年小明开办了一个农场，准备开始养母猪，
他专门给农场的母猪用以下数列2，3，4，5，7，9，12，16，21，28，37，49，65，86，114，151...进行命名。
假设农场的母猪永远不会死，小母猪出生后3年后成熟，成熟后从第三年开始每年只会生一只小母猪。
第一年农场，有一只刚刚出生的小母猪和一只成熟的母猪(本年不再生小猪，下一年开始生小猪)，并给他们编号为2和3。
请问，第m只母猪编号为多少？其是哪一年出生的？小明还准备了1份礼物，专门颁给农场第1到m只的母猪颁奖，
颁奖规则如下:选出第1到m只的母猪翻转编号(114编号翻转为411)为第k大的母猪进行颁奖，请问是第几只猪获奖？提示: f(n)=f(n-2)+f(n-3)
'''
m = 20
k = 3
n = []
n.append(2)
n.append(3)
n.append(4)
if m >= 3:
    for i in range(3, m):
        n.append(n[i-2]+n[i-3])
numberM = n[m-1]
N_big = 1
N_medium = 0
N_small = 1
year = 0
while N_big+N_medium+N_small < m:
    N_big += N_medium
    N_medium = N_small
    N_small = N_big
    year += 1
year += 2019
N = []



def flip(number, c):   #翻转函数
    a = number % 10
    c = c * 10
    c += a
    if number >= 10:
        b = int(number / 10)
        return flip(b, c)
    else:
        return c


for i in range(m):
    pig = [flip(n[i], 0)]
    pig.append(i+1)
    N.append(pig)


N.sort(key=lambda k:k[0])
award = N[m-k][1]
print('%d,%d,%d' %(numberM,year,award))
