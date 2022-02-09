import random
com = random.randint(1,20)
print("<< 컴퓨터가생각한1~20 숫자맞추기>>")
while True:
    player = int(input("숫자 입력(종료 0): "))
    if player == 0:
        break
    elif player == com:
        print("정답!!")
        break
    elif player > com :
        print("더 작은 숫자 입력! ")
    else:
        print("더 큰 숫자 입력")