from turtle import *

def makepolygon(n):
    for i in range(n):
        forward(100)
        left(360/n)

shape('turtle')
n=int(textinput('도형그리기','숫자입력(삼각형:3,사각형:4,오각형:5):'))
if n in[3,4,5]:
    makepolygon(n)
else:
    print('error')