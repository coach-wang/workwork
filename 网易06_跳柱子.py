'''
小易有n根柱子，第i根柱子的高度为hi。一开始小易站在第一根柱子上。小易能从第i根柱子跳到第j根柱子，当且仅当hi>=hj且1<=j-i<=k。
其中k为指定的一个数字。
另外小易拥有一次释放超能力的机会。这个超能力能让小易从柱子i跳到任意满足1<=j-i<=k的柱子而无视柱子高度的限制。
现在小易想知道，小易是否能到达第n根柱子。

输入描述:
第一行数据组数T
对于每组数据，第一行数字 n,k，接下来一行n个数字表示hi

输出描述:
对于每组数据，输出YES或NO
示例1
输入
1
5 3
6 2 4 3 8
输出
YES
示例2
输入
1
5 2
1 8 2 3 4
输出
NO
'''
'''
思路：从终点柱子出发，之前k个柱子中找到比他高的最矮的那个柱子，只要能到那个柱子就能到他，然后继续往前找，如果没有比他高的用一次超能力
到最矮的柱子继续找（但答案好像有问题）
'''
T = int(input().strip())
def judge(lis, k, used):
    height = lis[-1]
    if len(lis) <= k+1:
        if max(lis[:-1]) >= height or used == 0:
            return True
    else:
        limit = max(lis[-k-1:-1])
        if limit >= height:
            for i in lis[-k-1:-1]:
                if i >= height and i < limit:
                    limit = i
            ind = lis[-k-1:].index(limit)
            return judge(lis[:-k + ind], k, used)

        elif limit < height and used == 0:
            height = min(lis[-k-1:-1])
            ind = lis[-k - 1:].index(height)
            used = 1
            return judge(lis[:-k + ind], k, used)

        else:
            return False

for i in range(T):
    case = list(map(int, input().strip().split()))
    zhuzi = list(map(int, input().strip().split()))
    n, k = case[0], case[1]
    used = 0
    Flag = judge(zhuzi, k, used)
    if Flag == True:
        print('YES')
    else:
        print('NO')


