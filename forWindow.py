from tkinter import *
import webbrowser as wb
class Lessons:
    
    def __init__(self,master,name,link, lessonName,num):
        self.__lName = lessonName
        self.__link = link
        self.__name = name
        
        self.lesFrame = LabelFrame(master, text = self.__lName,bg="white")
        self.lesLab = Label(self.lesFrame, text = self.__name,width=20)
        self.lesBut = Button(self.lesFrame,
                             text = f"ссылка на урок {self.__name}",width=37)
            
        self.lesBut["command"] = self.gotolink
        
        #Флажок о выполнении
        self.varDone = BooleanVar()
        self.varDone.set(0)
        self.lesCheck = Checkbutton(master, text = "Выполнено", variable=self.varDone,
                              onvalue=1, offvalue=0, command=self.result)
        
        self.lesCheck.grid(row=num,column=1)
        self.lesFrame.grid(row=num,column=0)
        self.lesLab.grid(row=0,column=0)
        self.lesBut.grid(row=0,column=1)
        
    
    def gotolink(self):
        wb.open_new(rf"{self.__link}")
        
    def result(self):
        if (self.varDone.get() == 1):
            self.lesFrame["bg"] = "green"
        elif (self.varDone.get() == 0):
            self.lesFrame["bg"] = "white"