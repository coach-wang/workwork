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
#思路：  (要用python3)
# time_ideas字典
# while Ture:
#     time += 1
#     更新执行队列任务剩余时间
#     删除执行完的idea，更新程序员数量，记录完成时间
#     if 执行队列为空 and 所有idea = 0:
#         break
#     更新每个pm现有的idea
#     pm_ideas字典
#     while 还有程序员 并且 现有任务数 > 0：
#         找出每个pm现有的最想实现的idea
#         判断实现哪个idea，并加入执行队列,并从待执行队列中删除
#         任务数p -= 1
#         程序员数m -= 1
import sys

def Find_finish_time(time_ideas, M, P):
    time = 0
    processing_ideas = []
    finished_ideas = []
    pm_ideas_dic ={}  #pm提出的还未执行的idea字典
    n_remain_ideas = 0  #现有的idea数量
    while True:
        time += 1
        if processing_ideas != []:
            deleted_ideas = []
            for i in processing_ideas:
                i[3] -= 1
                if i[3] == 0:
                    deleted_ideas.append(i)
            for i in deleted_ideas:
                processing_ideas.remove(i)
                M += 1   #程序员完成任务，又可以执行下一个啦
                i.append(time)         #执行完成时间
                finished_ideas.append(i)
        
        if processing_ideas == [] and P == 0:   #所有idea都已提出并执行
            break
        
        for t in time_ideas:
            if t == time:
                for i in time_ideas[t]:    #t时刻提出的idea，即现有的idea
                    if i[0] not in pm_ideas_dic:
                        pm_ideas_dic[i[0]] = []
                    pm_ideas_dic[i[0]].append(i)
                    n_remain_ideas += 1
                break
        
        while M > 0 and n_remain_ideas > 0:
            pm_want_idea = []
            for i in pm_ideas_dic:
                if pm_ideas_dic[i] != []:   #每个pm最想实现的idea
                    pm_want_idea.append(min(pm_ideas_dic[i], key=lambda s:(-s[2], s[3], s[1])))
        
            if pm_want_idea != []:   #每个程序员优先执行的idea
                want_idea = min(pm_want_idea, key=lambda s:(s[3], s[0]))
                processing_ideas.append(want_idea)
                pm_ideas_dic[want_idea[0]].remove(want_idea)
                P -= 1
                n_remain_ideas -= 1
                M -= 1
                
    finished_ideas.sort(key=lambda k:k[4])
    for i in finished_ideas:
        print(i[5])
   
A = list(map(int, sys.stdin.readline().strip().split()))
N, M, P = A[0], A[1], A[2]
time_ideas = {}   #字典
for i in range(P):
    #0:pm序号 1:提出时间 2:优先等级 3:所需时间 4:任务序号 5：完成时间
    idea = list(map(int, sys.stdin.readline().strip().split()))
    idea.append(i)   
    if idea[1] not in time_ideas:
        time_ideas[idea[1]] = []   #按照提出时间的不同构建idea字典
    time_ideas[idea[1]].append(idea)   #添加上任务序号
Find_finish_time(time_ideas, M, P)
