'''
小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
你能帮帮小Q吗？

输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
  
输出描述:

对于每组数据，输出移位后的字符串。

输入例子1:
AkleBiCeilD

输出例子1:
kleieilABCD
'''
'''
思路：从后往前遍历，遇到大写字母往后交换位置
注意 大写字母的 ACSII码比小写字母小
'''
while True:
    try:
        string = list(input().strip())
        if string[-1] <= 'Z':
            big = 1
        else:
            big = 0
        for i in range(len(string) - 1):
            if string[len(string) - i - 2] <= 'Z':
                for j in range(len(string) - i - 2, len(string) - 1 - big):
                    t = string[j]
                    string[j] = string[j + 1]
                    string[j + 1] = t
                big += 1
        for i in string:
            print(i, end='')
        print('')
    except:
        break
