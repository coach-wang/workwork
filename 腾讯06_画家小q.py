'''
画家小Q又开始他的艺术创作。小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
小Q有他独特的绘画技巧,每次小Q会选择一条斜线, 如果斜线的方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,用'B'表示;
如果对角线的方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数N和M(1 <= N, M <= 50), 表示画板的长宽。
接下来的N行包含N个长度为M的字符串, 其中包含字符'B','Y','G','X',分别表示蓝色,黄色,绿色,空白。整个表示小Q要完成的作品。

输出描述:
输出一个正整数, 表示小Q最少需要多少次操作完成绘画。
示例1
输入
4 4
YXXB
XYGX
XBYY
BXXY
输出
3
'''
'''
思路：设置一个判断是否划过的矩阵
'''
nm = []
nm = list(map(int, input().strip().split()))
n, m = nm[0], nm[1]
picture = []
for i in range(n):
    picture.append(list(input().strip()))
y_done = [[0] * m for _ in range(n)]   #注意这里，不能用y_done = [[0]*m]*n,不然赋值会赋给整列
                                       #参考https://blog.csdn.net/zzc15806/article/details/82629406?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
b_done = [[0] * m for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if y_done[i][j] == 0:
            if picture[i][j] == 'Y' or picture[i][j] == 'G':
                count += 1
                a, b = i, j
                while a < n and b < m:
                    if picture[a][b] == 'Y' or picture[a][b] == 'G':
                        y_done[a][b] += 1
                        a += 1
                        b += 1
                    else:
                        break
        if b_done[i][m - j - 1] == 0 and (picture[i][m - j - 1] == 'B' or picture[i][m - j - 1] == 'G'):
            count += 1
            c, d = i, m - j - 1
            while c < n and d >= 0 and (picture[c][d] == 'B' or picture[c][d] == 'G'):
                b_done[c][d] += 1
                c += 1
                d -= 1

print(count)
