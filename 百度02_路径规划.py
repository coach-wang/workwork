'''
一个数轴上共有N个点，第一个点的坐标是度度熊现在位置，第N-1个点是度度熊的家。现在他需要依次的从0号坐标走到N-1号坐标。
但是除了0号坐标和N-1号坐标，他可以在其余的N-2个坐标中选出一个点，并直接将这个点忽略掉，问度度熊回家至少走多少距离？

输入描述:
输入一个正整数N, N <= 50。

接下来N个整数表示坐标，正数表示X轴的正方向，负数表示X轴的负方向。绝对值小于等于100

输出描述:
输出一个整数表示度度熊最少需要走的距离。

输入例子1:
4
1 4 -1 3

输出例子1:
4
'''
'''
思路：
忽略一个点只影响旁边的两个点，遍历一次找到减少最多的点即可
'''
n = int(input().strip())
p = list(map(int, input().strip().split()))
delta = 0
index = 0
for i in range(1, n-1):
    temp = abs(p[i]-p[i-1])+abs(p[i+1]-p[i])-abs(p[i+1]-p[i-1])
    if temp > delta:
        delta = temp
sum = 0
for i in range(n-1):
    sum += abs(p[i+1]-p[i])
sum -= delta
print(sum)

