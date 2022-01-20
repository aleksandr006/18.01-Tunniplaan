from tkinter import*
def uus_aken(ind:int):
    if askyesno("Küsimus","kas teen lahti?"):
        showinfo("vastus","Teen lahti aken")
    else:
        showinfo("Vastus","Panen kinnu aken")
        aken.destroy()
    uusaken=Toplevel() #tk()
    tabs=ttk.Notebook(uusaken)
    texts=[]
    textn=[]
    tab=[]
root=Tk()
#левые колонки
Button(text="Расписание LogITpv21").grid(row=0,column=1)#grid это вместо pack
Button(text="Понедельник:").grid(row=1,column=1)#grid это вертикальные столбики
Button(text="Вторник:").grid(row=2,column=1)#column горизонтальные столбики
Button(text="Среда:").grid(row=3,column=1)
Button(text="Четверг:").grid(row=4,column=1)
Button(text="Пятница:").grid(row=5,column=1)
#верхние колонки
Button(text="1").grid(row=0,column=2)
Button(text="2").grid(row=0,column=3)
Button(text="3").grid(row=0,column=4)
Button(text="4").grid(row=0,column=5)
Button(text="5").grid(row=0,column=6)
Button(text="6").grid(row=0,column=7)
Button(text="7").grid(row=0,column=8)
Button(text="8").grid(row=0,column=9)
Button(text="9").grid(row=0,column=10)
Button(text="10").grid(row=0,column=11)
#понедельник
Button(text=" Tugiõpe",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#4f4f4a").grid(row=1,column=2)# columnspan это объединение колонок
Button(text="Logistikateenused",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#2aa118").grid(row=1,column=3,columnspan=2)#width отвечает за ширину
Button(text="Matemaatika",relief=RIDGE,font="Arial 18",width=10,height=3,bg="#de52d0").grid(row=1,column=5)#height отвечает за высоту
Button(text="Matemaatika",relief=RIDGE,font="Arial 18",width=10,height=3,bg="#de52d0").grid(row=1,column=6)
Button(text="           ",font="Arial 20",width=10,height=3).grid(row=1,column=7)#пустой текст это перерыв
Button(text="Keel ja kirjandus",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#0eeb19").grid(row=1,column=8)
Button(text="Keel ja kirjandus",relief=RIDGE,font="Arial 18",width=10,height=3,bg="#0eeb19").grid(row=1,column=9)
Button(text="Tugiõpe",relief=RIDGE,font="Arial 18",width=10,height=3,bg="#ed4edd").grid(row=1,column=10)
#вторник
Button(text="Tugiõpe",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#990b8b").grid(row=2,column=2)
Button(text="Programmeerimise\n alused",relief=RIDGE,font="Arial 18",width=30,height=3,bg="#199cb0").grid(row=2,column=3,columnspan=3)
Button(text="           ",font="Arial 18",width=15,height=3).grid(row=2,column=6)
Button(text="Füüsika",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#de52d0").grid(row=2,column=7,columnspan=2)
#среда
Button(text=" Tugiõpe",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#de52d0").grid(row=3,column=2)
Button(text="Kunstained",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#990b8b").grid(row=3,column=3,columnspan=2)
Button(text="           ",font="Arial 18",width=10,height=3).grid(row=3,column=5)
Button(text="Kehaline kasvatus",relief=RIDGE,font="Arial 18",width=20,height=3,bg="#990b8b").grid(row=3,column=6,columnspan=2)
#четверг
Button(text="Logistikateenused",relief=RIDGE,font="Arial 18",width=20,height=3,bg="#2aa118").grid(row=4,column=2,columnspan=2)
Button(text="           ",font="Arial 18",width=10,height=3).grid(row=4,column=4)
Button(text="Programmeerimise\n alused",relief=RIDGE,font="Arial 18",width=20,height=3,bg="#199cb0").grid(row=4,column=5,columnspan=2)
Button(text="rakendus",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#e60e19").grid(row=4,column=7,columnspan=2)
Button(text="Eesti keel",relief=RIDGE,font="Arial 18",width=10,height=3,bg="#4f4f4a").grid(row=4,column=9)
Button(text="Eesti keel",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#4f4f4a").grid(row=4,column=10)
#пятница
Button(text="rakendus",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#b00c22").grid(row=5,column=2,columnspan=2)
Button(text="Programmeerimise alused",relief=RIDGE,font="Arial 18",width=65,height=3,bg="#199cb0").grid(row=5,column=4,columnspan=5)
Button(text="Inglise keel",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#0eeb19").grid(row=5,column=9)
Button(text="Inglise keel",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#0ee62e").grid(row=5,column=10)



root.mainloop()













