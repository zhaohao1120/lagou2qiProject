##定义有参数，有返回值
def clour1(clour='red'):
    print(clour)
    return clour

###定义无参数和无返回值
def  clour2(clour):
    if clour=='none':
        print('white')
    else:
        print(clour)


clour1()
clour2('black')
clour2('none')