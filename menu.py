import webbrowser
from pyautogui import press,click
import os
import pyaudio



#браузер
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
webbrowser.register('Chrome', None, webbrowser.BackgroundBrowser(chrome_path))
browser =  webbrowser.get('Chrome')
p = pyaudio.PyAudio()
def event(button):
        if(button =="youtube"):
            url = "https://youtube.com"
            browser.open_new(url)
        elif(button =="vk"):
            url = "https://vk.com"
            browser.open_new(url)
        elif(button =="google"):
            url = "https://google.com"
            browser.open_new(url)
        elif(button =="🤣"):
            url = "https://www.youtube.com/shorts/PjeRPKGSiTo"
            browser.open_new(url)
        elif(button =="space"):
            press("space")
        elif(button =="❌"):
            click(1910,10)
        elif(button =="⬅️"):
            for i in range(6):
                press("left")
        elif(button =="➡️"):
             for i in range(6):
                press("right")
        elif(isSymbol(button,".txt")):
            outputTextOnMonitor(button)
            os.startfile("file.txt")
            os.remove("file.txt")
        elif("%" in button):
            percent = button[1:]
            change_volume(percent)
        else:
            return "Нет такой команды :)"

def isSymbol(button,symbol):
    if button[:4] == symbol:
        return True


def outputTextOnMonitor(text):
    f = open("file.txt","w")
    f.write(text[4:])
    f.close()

def change_volume(volume_change):
    pass