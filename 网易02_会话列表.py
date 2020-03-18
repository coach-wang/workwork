'''
小云正在参与开发一个即时聊天工具，他负责其中的会话列表部分。
会话列表为显示为一个从上到下的多行控件，其中每一行表示一个会话，每一个会话都可以以一个唯一正整数id表示。
当用户在一个会话中发送或接收信息时，如果该会话已经在会话列表中，则会从原来的位置移到列表的最上方；
如果没有在会话列表中，则在会话列表最上方插入该会话。
小云在现在要做的工作是测试，他会先把会话列表清空等待接收信息。当接收完大量来自不同会话的信息后，就输出当前的会话列表，以检查其中是否有bug。
输入描述:
输入的第一行为一个正整数T（T<=10），表示测试数据组数。
接下来有T组数据。每组数据的第一行为一个正整数N（1<=N<=200），表示接收到信息的次数。
第二行为N个正整数，按时间从先到后的顺序表示接收到信息的会话id。会话id不大于1000000000。
输出描述:
对于每一组数据，输出一行，按会话列表从上到下的顺序，输出会话id。
相邻的会话id以一个空格分隔，行末没有空格。
输入例子1:
3
5
1 2 3 4 5
6
1 100 1000 1000 100 1
7
1 6 3 3 1 8 1
输出例子1:
5 4 3 2 1
1 100 1000
1 8 3 6
'''
'''
思路：
使用字典判断是否出现过会话即可
'''
import sys
T = int(sys.stdin.readline().strip())
talk = []
N = []
for i in range(T):
    N.append(int(sys.stdin.readline().strip()))
    talk.append(list(map(int, sys.stdin.readline().strip().split())))
for i in range(T):
    exist_talk = {}
    output = []
    n_output = 0
    for j in range(N[i]):
        if talk[i][N[i]-j-1] not in exist_talk:
            exist_talk[talk[i][N[i]-j-1]] = []
            output.append(talk[i][N[i]-j-1])
            n_output += 1
            # exist_talk[talk[i][N[i]-j-1]].append(j)
    for k in range(n_output-1):
        print(output[k], end=' ')    用空格分隔输出，不换行
    print(output[-1])  最后一个正常输出，换下一行
