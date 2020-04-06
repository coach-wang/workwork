'''
小易给定一个1到n的排列，希望你能求出这个序列中所有逆序对的距离和。
下标i,j的距离为|i-j|，逆序对是指序列中一对下标i,j满足i<j且ai>aj .

输入描述:
第一行数字n表示排列长度 
接下来一行n个数字表示这个排列

输出描述:
一行一个数字表示答案
示例1
输入
5  
1 3 4 2 5
输出
3
说明
逆序对:
(3, 2)距离为2
(4, 2)距离为1
总和为3
'''
'''
思路：类似暴力法，如果不是最大就往前遍历，运行超时（用二分法归并更好，可惜不会）
'''
n = int(input().strip())
lis = list(map(int, input().strip().split()))
Max = lis[0]
distance = 0
for i in range(n):
    if lis[i] < Max:
        for j in range(i):
            if lis[j] > lis[i]:
                distance += (lis[j]-lis[i])
    else:
        Max = lis[i]
print(distance)
