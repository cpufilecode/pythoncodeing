f=open('data1.txt')
lines=f.read()
print(lines)
f.close()

# with 구문 동일한 결과

with open('data1.txt') as f:
    lines=f.read()
    print(lines)