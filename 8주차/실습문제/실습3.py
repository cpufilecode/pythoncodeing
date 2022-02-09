n = int(input("수를 입력: "))
for i in range(1,n+1):
    if i%2 == 0:
        print(i,"짝수")
    else:
        print(i,"홀수")