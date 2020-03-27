'''
小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，
但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，表示父母出差的天数N(N<=50000)和巧克力的数量M(N<=M<=100000)。

输出描述:
输出一个数表示小Q第一天最多能吃多少块巧克力。

输入例子1:
3 7

输出例子1:
4
'''
'''
思路1：
假设第一天吃n块，M天下来一共吃了（1+1/2+...1/(2^(M-1))）*n块，考虑取整数，要用四舍五入，所以一共吃的块数肯定大于（1+1/2+...1/(2^(M-1))）*n
即n肯定小于M/（1+1/2+...1/(2^(M-1))）
然后从这个数开始往下找
但是只通过了70%
'''

P = []
P = list(map(int, input().strip().split()))
N, M = P[0], P[1]

def sum(N, vol):
    n = 0
    for i in range(N):
        n += vol
        vol = int(vol/2+0.5)
    return  n

base = 0
bbase = 1
for i in range(N):
    base += bbase
    bbase = bbase/2
vol = int(M/base)
while sum(N,vol) > M:
    vol = vol - 1
print(vol)

'''
思路2：使用二分法，时间复杂度更低
'''
P = []
P = list(map(int, input().strip().split()))
N, M = P[0], P[1]

def countSugar(num, k):
    sum = 0
    while k > 0:
        sum += num
        num = int(num/2+0.5)
        k -= 1
    return sum

left, right = 0, M
while left < right:
    mid = int((left + right)/2+0.5)
    if countSugar(mid, N) < M:
        left = mid
    elif countSugar(mid, N) > M:
        right = mid - 1  #注意这里要-1
    else:   #如果相等正好输出
        left = mid
        right = mid
print(left)
 

