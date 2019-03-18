# Complete the function below.
def  convert(number):
    res = ''
    dic = {
        0 : '0',
        1 : 'a',
        2: 't',
        3:'l',
        4:'s',
        5:'i',
        6:'n'
    }
    if number == 0:
        return 0
    while number != 0:
        tmp = number % 7
        number = number // 7
        res += dic[tmp]

    return res[::-1]

print(convert(0))