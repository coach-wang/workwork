'''
牛牛和羊羊正在玩一个纸牌游戏。这个游戏一共有n张纸牌, 第i张纸牌上写着数字ai。
牛牛和羊羊轮流抽牌, 牛牛先抽, 每次抽牌他们可以从纸牌堆中任意选择一张抽出, 直到纸牌被抽完。
他们的得分等于他们抽到的纸牌数字总和。
现在假设牛牛和羊羊都采用最优策略, 请你计算出游戏结束后牛牛得分减去羊羊得分等于多少。
输入描述:
输入包括两行。
第一行包括一个正整数n(1 <= n <= 105),表示纸牌的数量。
第二行包括n个正整数ai(1 <= ai <= 109),表示每张纸牌上的数字。

输出描述:
输出一个整数, 表示游戏结束后牛牛得分减去羊羊得分等于多少。

输入例子1:
3
2 7 4

输出例子1:
5
'''
'''
从大到小排序，奇数是牛，偶数是羊
'''
n = int(input().strip())
A = []
A = list(map(int, input().strip().split()))
A.sort(reverse=True)
number_cow = int((n+1)/2)
sum_cow = 0
number_sheep = int(n/2)
sum_sheep = 0
for i in range(number_cow):
    sum_cow += A[2*i]
for i in range(number_sheep):
    sum_sheep += A[2*i+1]
score = sum_cow - sum_sheep
print(score)
