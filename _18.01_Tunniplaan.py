from tkinter import *
root=Tk()
Button(text="Понедельник:").grid(row=1,column=1)
Button(text="Вторник:").grid(row=2,column=1)
Button(text="Среда:").grid(row=3,column=1)
Button(text="Четверг:").grid(row=4,column=1)
Button(text="Пятница:").grid(row=5,column=1)
Button(text="Суббота:").grid(row=6,column=1)
Button(text="Воскресенье:").grid(row=7,column=1)
root.mainloop()

Label(text="Имя:").grid(row=0,column=0)
table_name = Entry(width=30)
table_name.grid(row=0, column=1, columnspan=3)

Label(text="столбцов:").grid(row=1,column=0)
table_column =Spinbox(width=7,from_=1, to=50)
table_column.grid(row=1, column=1)
Label (text="строк").grid(row=1,column=2)
table_row = Spinbox(width=7,from_=1, to=100)
table_row.grid(row=1, column=3)
 
Button(text="справка").grid(row=2, column=0)
Button(text="вставить").grid(row=2, column=2)
Button(text="отменить").grid(row=2, column=3)

root.mainloop()