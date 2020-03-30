'''
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。

示例1
输入
0xA
输出
10
'''
#方法1：  当输入数量不确定的时候使用while True + try 
def count(s):
    n = 0
    for i in s:
        if i >= '0' and i <= '9':
            n = (n*16+int(i))
        if i >= 'A' and i <= 'F':
            temp = 10 + ord(i) - ord(('A'))   #ord()得到字符的ascii码
            n = (n*16+temp)
    return n

while True:
    try:
        a = list(input().strip())
        b = len(a)

        if a[0] == '-':
            n = -1 * count(a[3:])
        elif a[0] == '+':
            n = count(a[3:])
        else:
            n = count(a[2:])
        print(n)
    except:
        break

#方法2： 使用int函数来转化
while True:
    try:
        print(int(input(),16))
    except:
        break
