'''
产品经理(PM)有很多好的idea，而这些idea需要程序员实现。现在有N个PM，在某个时间会想出一个 idea，
每个 idea 有提出时间、所需时间和优先等级。对于一个PM来说，最想实现的idea首先考虑优先等级高的，
相同的情况下优先所需时间最小的，还相同的情况下选择最早想出的，没有 PM 会在同一时刻提出两个 idea。
同时有M个程序员，每个程序员空闲的时候就会查看每个PM尚未执行并且最想完成的一个idea,
然后从中挑选出所需时间最小的一个idea独立实现，如果所需时间相同则选择PM序号最小的。直到完成了idea才会重复上述操作。
如果有多个同时处于空闲状态的程序员，那么他们会依次进行查看idea的操作。求每个idea实现的时间。
输入第一行三个数N、M、P，分别表示有N个PM，M个程序员，P个idea。随后有P行，每行有4个数字，
分别是PM序号、提出时间、优先等级和所需时间。输出P行，分别表示每个idea实现的时间点。
输入描述:
输入第一行三个数N、M、P，分别表示有N个PM，M个程序员，P个idea。随后有P行，每行有4个数字，
分别是PM序号、提出时间、优先等级和所需时间。全部数据范围 [1, 3000]。
输出描述:
输出P行，分别表示每个idea实现的时间点。
输入例子1:
2 2 5
1 1 1 2
1 2 1 1
1 3 2 2
2 1 1 2
2 3 5 5
输出例子1:
3
4
5
3
9
'''
#思路：按照PM序号、所需时间、优先等级、提出时间进行分别进行排序，最后得到的就是每个idea排好的次序，然后按顺序执行即可
class Solution:
    def IdeaTime(self, matrix):
        N = matrix[0][0]
        M = matrix[0][1]
        P = matrix[0][1]
        for i in range(1, P+1):
            matrix[i].append(i)
        for i in range(1, P):   #先按PM序号排好
            for j in range(1, P+1-i):  #注意这里用冒泡排序来逐个交换，不然会打乱前后顺序
                if matrix[j][0] > matrix[j+1][0]:
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        for i in range(1, P):  #2 按所需时间排好
            for j in range(1, P+1-i)
                if matrix[j][3] > matrix[j+1][3]:
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        for i in range(1, P): #再按优先等级排好
            for j in range(1, P+1-i):
                if matrix[j][2] > matrix[j+1][2]:
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        for i in range(1, P):  #最后按提出时间排好（要先提出程序员才能执行）
            for j in range(1, P+1-i):
                if matrix[j][1] > matrix[j+1][2]:
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
        time = [0]*P
        for i in range(M):  #第一轮执行时间
            time[matrix[i+1][4]] += matrix[i+1][1]  # 先加上提出时间
            time[matrix[i+1][4]] += matrix[i+1][3]  #再加上所需时间
        for i in range(M, P):
            time[matrix[i+1][4]] += time[matrix[i+1-M][4]]   #加上之前经过的时间
            time[matrix[i+1][4]] += matrix[i+1][3]
        return time

        
