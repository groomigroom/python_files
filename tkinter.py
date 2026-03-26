from tkinter import *
from tkinter import messagebox

def myFunc() :
    messagebox.showinfo("경고", "주의하세요")

def myChec():
    if chk.get() == 0 :
        messagebox.showinfo("체크체크", "체크가 안되었어요.....")

    else :
        messagebox.showinfo("체크체크", "체크되었네요~~~!!!!")

root = Tk()

root.title("창 조절 연습")
root.geometry("500x200")
root.resizable(width=False, height=False)

label1 = Label(root, text="아아아")
label1.pack()
label2 = Label(root, text="열심히 공부하세요", font=("pretendard", 25), fg="green")
label2.pack()
label3 = Label(root, text="생일축하해요", font=("pretendard", 25), bg="#FFFFFF", fg="#333333", anchor=CENTER)
label3.place(x=120, y= 150)

button1 = Button(root, text="클릭", fg="#333333", command=myFunc)
button1.pack()

chk = IntVar()
cb1 = Checkbutton(root, text="체크", variable=chk, command=myChec)
cb1.pack()

root.mainloop()

#place
