from tkinter import *

root = Tk()

root.title("창 조절 연습")
root.geometry("500x200")
root.resizable(width=FALSE, height=FALSE)

label1 = Label(root, text="아아아")
label1.pack()
label2 = Label(root, text="열심히 공부하세요", font=("pretendard", 25), fg="green")
label2.pack()
label3 = Label(root, text="생일축하해요", font=("pretendard", 25), bg="#FFFFFF", fg="#333333", anchor=CENTER)
label3.pack()

root.mainloop()

#width=20, height=3, 
