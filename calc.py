ex1 = '5+10-2'

def calc(ex):
    plus = True
    minus = False
    tmp = ''
    rslt = 0
    while plus:
        minus = False
    while minus:
        plus = False
    for i in ex:
        if i in '0123456789':
            tmp += i
        elif i == '+':
            if plus:
                rslt += int(tmp)
                tmp = ''
            elif minus:
                rslt -= int(tmp)
                tmp = ''
    return rslt

calc(ex1)


