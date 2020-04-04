n = int(input().strip())
if n > 1000:
    n = 1000

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

data = []
for i in range(n):
    data.append(i)

l = LinkList()
l.initList(data)
t = l.head
for i in range(n):
    print(t.val)
    t = t.next
