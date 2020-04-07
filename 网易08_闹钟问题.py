'''
牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。从他起床算起他需要X分钟到达教室，
上课时间为当天的A时B分，请问他最晚可以什么时间起床

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
数据保证至少有一个闹钟可以让牛牛及时到达教室。

输出描述:
输出两个整数表示牛牛最晚起床时间。
示例1
输入
3 
5 0 
6 0 
7 0 
59 
6 59
输出
6 0
'''
'''
思路：排序即可解决
'''
n = int(input().strip())
clock = []
for i in range(n):
    clock.append(list(map(int, input().strip().split())))
x = int(input().strip())
time = []
for i in range(n):
    time.append(clock[i][0]*60 + clock[i][1])
time.sort()
lesson = list(map(int, input().strip().split()))
lesson_time = 60*lesson[0] + lesson[1]
for i in range(n):
    if time[n-1-i]+x <= lesson_time:
        get_time = time[n-1-i]
        break
output = [get_time//60, get_time % 60]
print(output[0], end=' ')
print(output[1])
