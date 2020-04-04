'''
有一个数组a[N]顺序存放0~N-1，要求每隔两个数删掉一个数，到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。以8个数(N=7)为例:｛0，1，2，3，4，5，6，7｝，0->1->2(删除)->3->4->5(删除)->6->7->0(删除),如此循环直到最后一个数被删除。

输入描述:
每组数据为一行一个整数n(小于等于1000)，为数组成员数,如果大于1000，则对a[999]进行计算。

输出描述:
一行输出最后一个被删掉的数的原始下标位置。

输入例子1:
8

输出例子1:
6
'''
'''
经典题目，构建环形链表来解决
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList(object):
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        p.next = self.head  #环形链表

while True:
    try:
        n = int(input().strip())
        if n > 1000:
            n = 1000
        data = []
        for i in range(n):
            data.append(i)

        l = LinkList()
        l.initList(data)
        t = l.head
        for i in range(n - 1):
            t = t.next
            temp = t.next
            temp = temp.next
            t.next = temp
            t = temp
        print(t.val)

    except:
        break
