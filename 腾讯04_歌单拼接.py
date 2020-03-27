'''
小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，现在小Q想用这些歌组成一个总长度正好为K的歌单，每首歌最多只能在歌单中出现一次，
在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
接下来的一行包含四个正整数，分别表示歌的第一种长度A(A<=10)和数量X(X<=100)以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。保证A不等于B。


输出描述:
输出一个整数,表示组成歌单的方法取模。因为答案可能会很大,输出对1000000007取模的结果。
示例1
输入
5
2 3 3 3
输出
9
'''
'''
思路：
分别按照A 0个 ，A 1个。。。依次排列组合，简单粗暴
'''
def comb(a, b):   #组合函数
    up = 1
    tempup = b
    while tempup > b - a:
        up = up * tempup
        tempup = tempup - 1
    down = 1
    tempdown = a
    while tempdown > 1:
        down = down * tempdown
        tempdown = tempdown - 1
    return up // down   #因为数字较大，这里要用 // 来除 而不是 /


def fix(K, A, B, X, Y, numA, numB):
    while numA * A + numB * B >= K and numB >= 0:
        if numA * A + numB * B == K:
            return comb(numA, X) * comb(numB, Y)
        else:
            numB = numB - 1
    return 0


K = int(input().strip())
P = []
P = list(map(int, input().strip().split()))
A, X, B, Y = P[0], P[1], P[2], P[3]

if A < B:  # 大的在前
    A, B = B, A
    X, Y = Y, X

numA, numB = X, Y
numCase = 0
sum = numA * A + numB * B

while sum >= K and numA >= 0:
    if sum == K:
        numCase += comb(numA, X)
    else:
        numCase += fix(K, A, B, X, Y, numA, numB)
    numA = numA - 1
    sum = numA * A + numB * B

output = (int(numCase)) % 1000000007  #数字较大的情况下取模

print(output)
