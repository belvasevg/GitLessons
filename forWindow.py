from tkinter import *
import webbrowser as wb
class Lessons:
    
    def __init__(self,master,name,link, lessonName,num):
        self.__lName = lessonName
        self.__link = link
        self.__name = name
        
        self.__lesFrame = LabelFrame(master, text = self.__lName,bg="white")
        self.__lesLab = Label(self.__lesFrame, text = self.__name,width=20)
        self.__lesBut = Button(self.__lesFrame,
                             text = f"ссылка на урок {self.__name}",width=37)
            
        self.__lesBut["command"] = self.__gotolink
        
        #Флажок о выполнении
        self.__varDone = BooleanVar()
        self.__varDone.set(0)
        self.__lesCheck = Checkbutton(master, text = "Выполнено", variable=self.__varDone,
                              onvalue=1, offvalue=0, command=self.__result)
        
        self.__lesCheck.grid(row=num,column=1)
        self.__lesFrame.grid(row=num,column=0)
        self.__lesLab.grid(row=0,column=0)
        self.__lesBut.grid(row=0,column=1)
        
    
    def __gotolink(self):
        wb.open_new(rf"{self.__link}")
        
    def __result(self):
        if (self.__varDone.get() == 1):
            self.__lesFrame["bg"] = "green"
        elif (self.__varDone.get() == 0):
            self.__lesFrame["bg"] = "white"