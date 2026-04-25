from tkinter import *
from tkinter import messagebox
from tkmacosx import Button
from tkinter import font

full = Tk()


full.title("현재 시간")
full.geometry("500x500")
full.resizable(width=False, height=False)

bg_img = PhotoImage(file="img/background.png")

bg_label = Label(full, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

def alert():
    dnow = datetime.now()
    btn.config(text = dnow)

btn_font = font.Font(family="pretendard", size=12, weight="bold")

btn = Button(full)
btn.config(
    text = '현재 시각',
    borderless=1,
    focuscolor='',
    highlightthickness=0
    #배경 검정색 없에는 3가지 속성
           )
btn.config(width = 300, height=30, font=btn_font, bg="#AAAAAA", fg="#333333")
btn.config(command = alert)

btn.place(relx=0.5, y=300, anchor='center')
btn.lift()

from datetime import datetime
print(datetime.now())

full.mainloop()
