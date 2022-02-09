addr = {}

while True:
    s=int(input("1) 친구등록 2) 검색 3) 종료 : "))
    if s==1:
        name=input("name:")
        phone=input("phone:")
        addr [name]=phone
    elif s==2:
        name=input("name:")
        print(addr.get(name,"not found"))
    elif s==3:
        print("end")
        break
    else:
        print("menu error")