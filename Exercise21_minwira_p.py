from tkinter import *
import math
def leftClickButton(event) :
    print(float(textBoxweigt.get()) / math.pow(float(textBoxHight.get()) / 100, 2))
    result = (format(float(textBoxweigt.get())/math.pow(float(textBoxHight.get())/100, 2), '.2f'))
    levelbmi = ""

    if float(result) >= 30.0:
        levelbmi = "อ้วนมาก"
    elif float(result) >= 25.0:
        levelbmi = "น้ำหนักเกิน"
    elif float(result) >= 23.0:
        levelbmi = "น้ำหนักปกติ"
    elif float(result) >= 18.6:
        levelbmi = "ผอมเกินไป"
    elif float(result) <= 18.5:
        levelbmi = "ผอมเกินไป"

    levelresult.configure(text=levelbmi)
    labelresult.configure(text=result)
    
MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง(cm.)")
labelHeight.grid(row=0,column=0)
textBoxHight = Entry(MainWindow)
textBoxHight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก(kg)")
labelWeight.grid(row=1,column=0)
textBoxweigt = Entry(MainWindow)
textBoxweigt.grid(row=1,column=1)
calculateButton = Button(MainWindow,width=15,text="คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2)
labelresult = Label(MainWindow,text="ผลลัพธ์")
labelresult.grid(row=2,column=1)
levelresult = Label(MainWindow,text="ระดับ")
levelresult.bind('<Button-1>',leftClickButton)
levelresult.grid(row=3,column=1)

MainWindow.mainloop()
