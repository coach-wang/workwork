'''
有三种葡萄，每种分别有 a,b,c颗。有三个人，第一个人只吃第 1,2种葡萄，第二个人只吃第2,3种葡萄，
第三个人只吃第 1,3种葡萄。
适当安排三个人使得吃完所有的葡萄,并且且三个人中吃的最多的那个人吃得尽量少。

输入描述:
第一行数字T，表示数据组数。
接下来T行，每行三个数 a,b,c

输出描述:
对于每组数据，输出一行一个数字表示三个人中吃的最多的那个人吃的数量。
示例1
输入
2
1 2 3
1 2 6
输出
2
3
示例2
输入
1
12 13 11
输出
12
'''
'''
思路：满足情况最好是让三个人吃的接近（即接近总数的1/3），所以先把3种葡萄按数量大小排序，
数量最少的两种葡萄先满足第“一”个人，给他喂够1/3之后剩下的给两个人平分；如果第一个人喂不够1/3，那么尽量满足他，剩下的让两个人平分
'''
T = int(input().strip())
for i in range(T):
    grape = list(map(int, input().strip().split()))
    grape.sort()
    a, b, c = grape[0], grape[1], grape[2]
    Sum = a + b + c
    medium = Sum//3
    if b >= (medium-a):
        b = b-medium+a
        Medium = (b+c)//2
        c = Sum-medium-Medium
    else:
        Medium = c//2
        c = c-Medium
    print(c)

