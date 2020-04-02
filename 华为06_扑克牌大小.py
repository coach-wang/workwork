'''
扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A，2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示
（其中，小写joker表示小王，大写JOKER表示大王）:)
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格，如：4 4 4 4-joker JOKER
请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR

基本规则：
（1）输入每手牌可能是个子，对子，顺子（连续5张），三个，炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，
顺子已经从小到大排列；
（2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），
不考虑拆牌情况（如：将对子拆分成个子）
（3）大小规则跟大家平时了解的常见规则相同，个子，对子，三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；
对王是最大的牌；
（4）输入的两手牌不会出现相等的情况。

答案提示：
（1）除了炸弹和对王之外，其他必须同类型比较。
（2）输入已经保证合法性，不用检查输入是否是合法的牌。
（3）输入的顺子已经经过从小到大排序，因此不用再排序了.

输入描述:
输入两手牌，两手牌之间用“-”连接，每手牌的每张牌以空格分隔，“-”两边没有空格，如4 4 4 4-joker JOKER。


输出描述:
输出两手牌中较大的那手，不含连接符，扑克牌顺序不变，仍以空格隔开；如果不存在比较关系则输出ERROR。
示例1
输入
4 4 4 4-joker JOKER
输出
joker JOKER
'''
'''
建立一个list，判断他们的index即可比较大小
如果不是王炸，其他比较必须数目一样，直接比第一个数就行，数目不一样就是error
'''
card_list = list(input().strip().split('-'))
card1 = card_list[0].split(' ')
card2 = card_list[1].split(' ')
rule = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'joker', 'JOKER']

def if_Boom(lis):
    flag = 0
    if len(lis) == 4:
        flag = 1
    elif len(lis) == 2:
        if lis[0] == 'joker' and lis[1] == 'JOKER':
            flag = 2
        elif lis[0] == 'JOKER' and lis[1] == 'joker':
            flag = 2
    return flag

def judge(a, b):
    if rule.index(a[0]) > rule.index(b[0]):
        return a
    else:
        return b

if if_Boom(card1) > if_Boom(card2):
    winner = card1
elif if_Boom(card1) < if_Boom(card2):
    winner = card2
else:
    if len(card1) == len(card2):
        winner = judge(card1, card2)
    else:
        winner = 0

if winner == 0:
    print('ERROR')
else:
    for i in winner[:-1]:
        print(i, end=' ')
    print(winner[-1])
