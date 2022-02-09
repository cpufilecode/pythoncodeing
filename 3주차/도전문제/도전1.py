#분과 초를 출력하는 문제

total = int(input ('시간의전체초입력:'))
min = total // 60
sec = total % 60
print('%d 초: %d 분%d 초'% (total, min, sec))