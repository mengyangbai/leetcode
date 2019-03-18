
def compute(instructions):
    stack = [0 for _ in range(9)]
    haveblock = False
    currentstage = 0
    for ac in instructions:
        if ac == 'P':
            haveblock = True
            currentstage = 0
        elif ac == 'M':
            if currentstage != 9:
                currentstage += 1

        elif ac == 'L':
            if stack[currentstage] != 15:
                if haveblock:
                    haveblock = False
                    stack[currentstage]+=1

    res = ''

    dic ={
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'
    }
    for num in stack:
        if num in dic:
            res+=dic[num]
        else:
            res+=str( num)

    
    return res

print(compute("PLPLPLPLPLPLPLPLPLPL"))