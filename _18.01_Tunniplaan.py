from tkinter import*
root=Tk()
root.title("tunni plan")
root.geometry("1800x1000+100+100")
root.resizable(width=False, height=False)
 
def Eestikeel():
  label.configure(text="Eesti keel - õpetaja: Ojamäe Olesja B 234",font="Arial 20")
def Logistika():
  label.configure(text="Logistika - õpetaja: Klimanskaja Inessa B 002",font="Arial 20")
def Matematika():
  label.configure(text="Matemaatika - õpetaja: Voronova Nadezda B 133 ",font="Arial 20")
def Venekell():
  label.configure(text="Venekeel- õpetaja: Mihhailova Ljudmila B 221",font="Arial 20")
def programeriumine():
  label.configure(text="Programmeerimise alused - õpetaja: Oleinik Marina E 07",font="Arial 20")
def Füüsika():
  label.configure(text="Füüsika - õpetaja: Voronova Nadezda B 133",font="Arial 20")
def Inglisekeel():
  label.configure(text="Inglise keel - õpetaja: Borodina Olga B 227",font="Arial 20")
def Kunst():
  label.configure(text="Kunst - õpetaja: Norkevitð Aleksandra B 232",font="Arial 20")
def kehaline():
  label.configure(text="Kehaline Kasvatus - õpetaja: Maksõmiv Maksim Võimla A",font="Arial 20")
def Rakendus():
  label.configure(text="Rakendus- õpetaja: Merkulova Irina E 10",font="Arial 20")
label = Label(root)
label.place(x=700, y=600)

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
Button(text=" Tugiõpe",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#4f4f4a").grid(row=1,column=2,sticky=W+E+N+S)# columnspan это объединение колонок
Button(text="Logistika",relief=RIDGE,font="Arial 18",width=20,height=3,bg="#2aa118",command=Logistika).grid(row=1,column=3,columnspan=2,sticky=W+E+N+S)#width отвечает за ширину
Button(text="Matemaatika",relief=RIDGE,font="Arial 18",width=30,height=3,bg="#de52d0",command=Matematika).grid(row=1,column=5,columnspan=2,sticky=W+E+N+S)#height отвечает за высоту
Button(text="           ",font="Arial 18",width=15,height=3).grid(row=1,column=7)#пустой текст это перерыв
Button(text="Keel ja kirjandus",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#0eeb19",command=Venekell).grid(row=1,column=8,sticky=W+E+N+S)
Button(text="Keel ja kirjandus",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#0eeb19",command=Venekell).grid(row=1,column=9,sticky=W+E+N+S)
#вторник
Button(text="Tugiõpe",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#990b8b",).grid(row=2,column=2,sticky=W+E+N+S)
Button(text="Programmeerimine",relief=RIDGE,font="Arial 18",width=40,height=3,bg="#199cb0",command=programeriumine).grid(row=2,column=3,columnspan=3,sticky=W+E+N+S)
Button(text="           ",font="Arial 18",width=15,height=3).grid(row=2,column=6,sticky=W+E+N+S)
Button(text="Füüsika",relief=RIDGE,font="Arial 18",width=30,height=3,bg="#de52d0",command=Matematika).grid(row=2,column=7,columnspan=2,sticky=W+E+N+S)
#среда
Button(text=" Tugiõpe",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#de52d0").grid(row=3,column=2,sticky=W+E+N+S)
Button(text="Kunst",relief=RIDGE,font="Arial 18",width=20,height=3,bg="#990b8b",command=Kunst).grid(row=3,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="           ",font="Arial 18",width=15,height=3).grid(row=3,column=5,sticky=W+E+N+S)
Button(text="Kehaline kasvatus",relief=RIDGE,font="Arial 18",width=30,height=3,bg="#990b8b",command=kehaline).grid(row=3,column=6,columnspan=2,sticky=W+E+N+S)
#четверг
Button(text="Logistika",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#2aa118",command=Logistika).grid(row=4,column=2,columnspan=2,sticky=W+E+N+S)
Button(text="           ",font="Arial 18",width=15,height=3).grid(row=4,column=4,sticky=W+E+N+S)
Button(text="Programmeerimine",relief=RIDGE,font="Arial 18",width=35,height=3,bg="#199cb0",command=programeriumine).grid(row=4,column=5,columnspan=2,sticky=W+E+N+S)
Button(text="rakendus",relief=RIDGE,font="Arial 18",width=30,height=3,bg="#e60e19",command=Rakendus).grid(row=4,column=7,columnspan=2,sticky=W+E+N+S)
Button(text="Eesti keel",relief=RIDGE,font="Arial 18",width=25,height=3,bg="#4f4f4a",command=Eestikeel).grid(row=4,column=9,columnspan=2,sticky=W+E+N+S)
#пятница
Button(text="rakendus",relief=RIDGE,font="Arial 18",width=15,height=3,bg="#b00c22",command=Rakendus).grid(row=5,column=2,columnspan=2,sticky=W+E+N+S)
Button(text="Programmeerimine",relief=RIDGE,font="Arial 15",width=83,height=3,bg="#199cb0",command=programeriumine).grid(row=5,column=4,columnspan=5,sticky=W+E+N+S)
Button(text="Inglise keel",relief=RIDGE,font="Arial 15",width=30,height=3,bg="#0eeb19",command=Inglisekeel).grid(row=5,column=9,columnspan=2,sticky=W+E+N+S)



root.mainloop()





