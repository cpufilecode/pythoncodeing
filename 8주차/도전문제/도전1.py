while True:
    num= int(input('수를입력: '))
    if num == 0:
        print('종료')
        break
    elif num%2 == 0:
        print('짝수')
    else:
        print('홀수')