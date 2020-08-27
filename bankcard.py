from random import randint
from random import choice

def randombin():
    list19 = [622546, 622547, 622548, 622561, 622562, 622563, 622681, 622682, 622700, 622770, 622821, 622822, 622823, 622824, 622825, 622826, 622840, 622844, 622845, 622846, 622847, 622848, 622855, 622857, 622858, 622859, 622865, 622869, 622877, 622879, 622882, 622891, 622893, 622897]
    # list16 = [622538, 622549, 622550, 622580, 622588, 622598, 622615, 622617, 622619, 622622, 622630, 622631, 622632, 622633, 622660, 622684, 622690, 622691, 622692, 622696, 622698, 622777, 622860, 622861, 622864, 622866, 622867, 622870, 622871, 622880, 622881, 622884, 622885, 622886, 622895,622909]
    str1 = choice(list19)
    return str(str1)

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

# def oddeven16(string):
#     s = 0
#     for i in range(0,len(string)):
#         if(i % 2 == 0):
#             t = int(string[i]) * 2
#             if (t >= 10):
#                 t = t // 10 + t % 10
#         else:
#             t = int(string[i])
#         s = s + t
#     return s

def lastnum(s):
    if (s % 10 != 0):
        t = (s // 10 +1) * 10 - s
    else:
        t = 0
    return str(t)

if __name__ == "__main__":
    str1 = randombin()
    str2 = randomnums()
    str3 = str1+str2
    s = oddeven19(str3)
    strx = str(lastnum(s))
    cardnum = str1 + str2 + strx
    print(cardnum)