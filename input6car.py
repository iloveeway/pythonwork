from random import randint
import re

def randomnums():
    s = ""
    for i in range(0,12):
        t = randint(0,9)
        s = s+(str(t))
    return s

def oddeven19(string):
    s = 0
    for i in range(0,len(string)):
        if(i % 2 != 0):
            t = int(string[i]) * 2
            if (t >= 10):
                t = t // 10 + t % 10
        else:
            t = int(string[i])
        s = s + t
    return s

def lastnum(s):
    if (s % 10 != 0):
        t = (s // 10 +1) * 10 - s
    else:
        t = 0
    return str(t)

if __name__ == "__main__":
    print("请输入6位BIN码：")
    while(1):
        str1 = input()
        if not re.match(r'^62\d{4}$',str1):
            print("只能输入6位数字字符，且以62开头。")
            print("请输入6位BIN码：")
        else:
            break
    
    str2 = randomnums()
    str3 = str1+str2
    s = oddeven19(str3)
    strx = str(lastnum(s))
    cardnum = str1 + str2 + strx
    print(cardnum)