from tkinter import *
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

#esmaspäev
Button(text="Tugiõpe gr2").grid(row=1,column=2)
Button(text="logistika").grid(row=1,column=3,columnspan=2)# columnspan это объединение колонок
Button(text="matematika").grid(row=1,column=5,columnspan=2)
Button(text="    ").grid(row=1,column=7)#пустой текст это перерыв
Button(text="vene keel").grid(row=1,column=8,columnspan=2)
#teisipäev
Button(text="Tugiõpe keemia").grid(row=2,column=2)
Button(text="Programeriumine").grid(row=2,column=3,columnspan=3)
Button(text="    ").grid(row=2,column=6)
Button(text="Füüsika").grid(row=2,column=7,columnspan=2)
#kolmapäev
Button(text="Tugiõpe gr1").grid(row=3,column=2)
Button(text="Kunst:").grid(row=3,column=3,columnspan=2)
Button(text="    ").grid(row=3,column=5)
Button(text="Физра").grid(row=3,column=6,columnspan=2)
#neljapäev
Button(text="logistika").grid(row=4,column=2,columnspan=2)
Button(text="    ").grid(row=4,column=4)
Button(text="Programeriumine").grid(row=4,column=5,columnspan=2)
Button(text="rakendus").grid(row=4,column=7,columnspan=2)
Button(text="eesti keel").grid(row=4,column=9,columnspan=2)
Button(text="ruhma tund").grid(row=4,column=11)
#rede
Button(text="rekendus").grid(row=5,column=2,columnspan=2)
Button(text="Programeriumine").grid(row=5,column=4,columnspan=5)
Button(text="inglise keel").grid(row=5,column=9,columnspan=2)


root.mainloop()
