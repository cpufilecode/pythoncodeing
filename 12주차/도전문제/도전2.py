from tkinter import *
from tkinter.messagebox import *

def login():
    if sid.get() == "cpu":
        if spw.get()=="1234":
            showinfo("success", "로그인성공")
        else:
            showinfo("fail", "패스워드 오류")
    else:
            showinfo("fail", "회원가입!!")

w=Tk()
w.title("welcome!!") 
logo=Label(w,text="login program")
sid=Entry(w)
spw=Entry(w,show="●")
btn1=Button(w, text="LOGIN", command=login)

logo.pack()
sid.pack()
spw.pack()
btn1.pack()