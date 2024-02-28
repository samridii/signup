from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Add Income Page")
window.config(bg='#658d6d')
window.maxsize(width=760,height=490)
window.minsize(width=760,height=490)

#creating frame
frame1=Frame(window,width=200,height=440)
frame1.config(bg="white") 
frame1.place(x=20,y=20)

#adding labels in frame 1
add_income=Button(frame1,text="Add Income",borderwidth=0,bg='white')
add_expenses=Button(frame1,text="Add Expenses",borderwidth=0,bg="#96ae8d")
view_report=Button(frame1, text="View Report", borderwidth=0,bg='white')

#placing labels in frame 1
add_income.place(x=20,y=160)
add_expenses.place(x=20,y=190)
view_report.place(x=20,y=220)

#creating frame 2
frame2=Frame(window,width=480,height=440)
frame2.config(bg="white") 
frame2.place(x=250,y=20)

#creating labels
total_label=Label(frame2,text="Total Income:",bg='#96ae8d',font=("Hubballi",20),width=25)
income_title=Entry(frame2,bg='#96ae8d',fg="#363737",font=('Hubbali',12))
income_title.insert(0, "     Income Title")
income_amount=Entry(frame2,bg='#96ae8d',fg="#363737",font=('Hubbali',12))
income_amount.insert(0, "     Income Amount")
income_type=Entry(frame2, bg='#96ae8d',fg="#363737",font=('Hubbali',12))
income_type.insert(0, "     Income Type")
add_income=Button(frame2, text="Add Income",font=('Hubbali',12))

#place labels
total_label.place(x=40,y=40)
income_title.place(x=40,y=100)
income_amount.place(x=40,y=140)
income_type.place(x=40,y=180)
add_income.place(x=40,y=230)



window.mainloop()

