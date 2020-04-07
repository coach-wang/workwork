'''
平面内有n个矩形, 第i个矩形的左下角坐标为(x1[i], y1[i]), 右上角坐标为(x2[i], y2[i])。
如果两个或者多个矩形有公共区域则认为它们是相互重叠的(不考虑边界和角落)。
请你计算出平面内重叠矩形数量最多的地方,有多少个矩形相互重叠。

输入描述:
输入包括五行。
第一行包括一个整数n(2 <= n <= 50), 表示矩形的个数。
第二行包括n个整数x1[i](-10^9 <= x1[i] <= 10^9),表示左下角的横坐标。
第三行包括n个整数y1[i](-10^9 <= y1[i] <= 10^9),表示左下角的纵坐标。
第四行包括n个整数x2[i](-10^9 <= x2[i] <= 10^9),表示右上角的横坐标。
第五行包括n个整数y2[i](-10^9 <= y2[i] <= 10^9),表示右上角的纵坐标。

输出描述:
输出一个正整数, 表示最多的地方有多少个矩形相互重叠,如果矩形都不互相重叠,输出1。
示例1
输入
2
0 90
0 90
100 200
100 200
输出
2
'''
'''
思路：
先读取每个矩形，框出所有矩形的大边界。然后在这个大边界中逐个点判断有几个矩形在此重叠，但是运行超时了
'''
n = int(input().strip())
x1 = list(map(int, input().strip().split()))
y1 = list(map(int, input().strip().split()))
x2 = list(map(int, input().strip().split()))
y2 = list(map(int, input().strip().split()))
left = min(x1)
right = max(x2)
botton = min(y1)
up = max(y2)
same = 0
def count_inbox(x, y, a1, b1, a2, b2, n):
    box = 0
    for i in range(n):
        if x >= a1[i] and x <= a2[i] and y >= b1[i] and y <= b2[i]:
            if x+1 >= a1[i] and x+1 <= a2[i] and y >= b1[i] and y <= b2[i]:   #这里再添加一次判断，是为了避免两个矩形只有一个点重合的情况，
                                                                                #这种不算重叠
            
                box += 1

    return box


for i in range(left, right+1):
    for j in range(botton, up+1):
        n_box = count_inbox(i, j, x1, y1, x2, y2, n)
        if n_box > same:
            same = n_box
print(same)
