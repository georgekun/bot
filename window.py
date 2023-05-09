from tkinter import *
import os

const_password = 'jorj159951'


def deleteWindow():
  os._exit(1)
    

def createWindow():
  
  root=Tk()
  
  root.state('zoomed')
  root.attributes('-topmost',True) #всегда выше всех экранов пиздец
  # root.maxsize(1102,1001)
  root.title("Экран заблокирован")
  root.overrideredirect(1)
  #default password
 
  #ввод пароля
  message = Label(text="Введи пароль для разблокировки")
  message.pack(pady="300")
  input = Entry()
  input.pack()

  #проверка введенного пароля
  def close(): 
      if(input.get() == const_password):
        root.destroy()
      else:
        message = Message(text="пароль неверен").pack()
        
        
  button = Button(root,text="Выйти",command=close)
  button.pack()
  

# это заглушка. пасс это ничто
  def Quit():
    pass
 
  #root.protocol("WM_DELETE_WINDOW",quit)
  root.mainloop()


