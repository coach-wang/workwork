'''
小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，相差最小的有多少对呢？相差最大呢？

输入描述:

 输入包含多组测试数据。
 对于每组测试数据：
 N - 本组测试数据有n个数
 a1,a2...an - 需要计算的数据
 保证:
 1<=N<=100000,0<=ai<=INT_MAX.
  
输出描述:

对于每组数据，输出两个数，第一个数表示差最小的对数，第二个数表示差最大的对数。

示例1
输入
6
45 12 45 32 5 6
输出
1 2
'''
'''
思路：对输入数组排序，从前往后遍历找最小的差并统计数量，如果最小差值是0，那么对数要用(n+1)n/2来计算（比如2, 2, 2, 2 有6对）
最大差的对数就是最大值的数量乘最小值的数量
'''
n = int(input().strip())
an = list(map(int, input().strip().split()))
an.sort()
delta_min = an[1] - an[0]
n_min = 1
for i in range(2, n):
    if delta_min == 0:
        break
    if an[i] - an[i-1] < delta_min:
        delta_min = an[i] - an[i-1]
        n_min = 1
    if an[i] - an[i-1] == delta_min:
        n_min += 1
if delta_min == 0:
    t = 1
    n_min = 0
    for i in range(1, n):
        if an[i] == an[i-1]:
            t += 1
        else:
            n_min += (t-1)*t//2
            t == 1
    n_min += (t - 1) * t // 2


min_n = 1
for i in range(1, n):
    if an[i] == an[0]:
        min_n += 1
    else:
        break
max_n = 1
for i in range(1, n):
    if an[n-1-i] == an[-1]:
        max_n += 1
    else:
        break
n_max = min_n*max_n
print(n_min, end=' ')
print(n_max)
