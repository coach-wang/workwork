'''
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。

输入描述:
输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
  
输出描述:
对于每组数据，输出一个整数，代表最少需要删除的字符个数。

示例1
输入
abcda
google
输出
2
2
'''
'''
思路：以第一个字母为开头开始找，得到的长度为m，然后从这个字母往后为开头依次找到最大的长度
'''
def build(lis):
    if len(lis) == 1:  
        return 1
    elif len(lis) == 2 and lis[0] == lis[1]:
        return 2
    else:
        for i in range(len(lis)-2):
            if lis[len(lis)-i-1] == lis[0]:
                return build(lis[1:len(lis)-i-1])+2
        return build(lis[1:])

while True:
    try:
        s = list(input().strip())
        n = build(s)
        m = n
        for i in range(1, len(s)-n):   #这里到len（s）-n即可，因为剩下的长度也不会超过n
            t = build(s[i:])
            if t > m:
                m = t
        print(len(s)-m)
    except:
        break
