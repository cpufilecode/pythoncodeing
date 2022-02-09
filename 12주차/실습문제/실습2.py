from tkinter import*
from tkinter import messagebox


def login():
    if pw.get()=="1234":
        messagebox.showinfo("success","로그인 성공")
    else:
        messagebox.showinfo("fail","패스워드 오류")
w=Tk()
w.title("패스워드가 입력되었습니다.")

label1=Label(w,text='패스워드')
pw=Entry(w,show='*')
btn1=Button(w,text='확인',command=login)
btn2=Button(w,text='종료',command=quit)

label1.pack()
pw.pack()
btn1.pack()
btn2.pack()
w.geometry('300x200')
