# from tkinter import *
# from tkinter.ttk import *
# import time

# progressBarTime = 45
# root = Tk()
# ran = False
# progress = Progressbar(root, orient = HORIZONTAL, length = 100, mode = 'determinate',maximum=100,value=5)
# progress.pack(pady = 10)

# def bar():
#     length = progressBarTime*60
#     initialTime = 0
#     while(initialTime<length):
#         if((initialTime%27)==0):
#             print('percentage at '+str(initialTime)+" seconds")
#             progress.step(1000)
#         initialTime+=1
#         print(initialTime)
#         time.sleep(1)

  

  
# # This button will initialize
# # the progress bar
# if(not ran):
#     bar()
#     ran = True
  
# # infinite loop
# mainloop()

















from tkinter import *
from tkinter.ttk import *
import time

progressBarTime = 45
title = "Download"
root = Tk()
root.title( title)
ran = False
textr = StringVar()
label = Label(root,textvariable=textr)
textr.set("Downloading...")
var1 = DoubleVar(root)
progress = Progressbar(root, orient = HORIZONTAL, length = 600, mode = 'determinate',maximum=(progressBarTime*60),variable=var1)
label.pack(pady=(30,0))
progress.pack(padx = 30,pady=(10,40))


def bar():
    progress.start(1000)

def newMessage():
    progress.stop()
    textr.set("Download Complete!")
    button = Button(root,text="Close Window",command=doTheQuit)
    button.pack(pady=(0,25))

def doTheQuit():
    root.quit()

  
# This button will initialize
# the progress bar
if(var1.get()<=100):
    bar()
ran = True

root.after(int((progressBarTime*60-1)*1000),newMessage)
  
# infinite loop
mainloop()



















# from tkinter import *
# from tkinter.ttk import *
# import threading
# import time

# threading.Thread
# progressBarTime = 45
# root = Tk()

# # create progressbar
# variable = DoubleVar(root)

# ran = False
# label = Label(root,text="Downloading...")
# pP = StringVar()
# progress = Progressbar(root, orient = HORIZONTAL, length = 600, mode = 'determinate',maximum=(progressBarTime*60),value=5,variable=variable)
# progressPercentage = Label(root,textvariable=pP)
# label.pack(pady=(30,0))
# progress.pack(padx = 30,pady=(10,40))
# progressPercentage.pack()


# def bar():
#     init = 0
#     while(init<=progressBarTime*60):
#         progress.step()
#         pP.set(str(((variable.get()/2700)*100)))
#         root.update()
#         init+=1
#         time.sleep(1)
    

  

  
# # This button will initialize
# # the progress bar
# if(not ran):
#     bar()
#     ran = True
  
# # infinite loop
# mainloop()









# class ProgressBar(threading.Thread):
#     def __init__(self):
#         # threading.Thread.__init__(self)
#         self.title = "Some Other Download"
#         self.progressBarTime = 45
#         self.value = 0
    
#     def start(self):
#         self.root = Tk()
#         self.variable = DoubleVar(self.root)

#         self.label = Label(self.root,text="Downloading...")
#         self.pP = StringVar()
#         self.progress = Progressbar(self.root, orient = HORIZONTAL, length = 600, mode = 'determinate',maximum=(self.progressBarTime*60),value=5,variable=self.variable)
#         self.progressPercentage = Label(self.root,textvariable=self.pP)
#         self.label.pack(pady=(30,0))
#         self.progress.pack(padx = 30,pady=(10,40))
#         self.progressPercentage.pack()

#         self.startProgress()
#         self.root.mainloop()
    
#     def startProgress(self):
#         init = 0
#         while(init<=self.progressBarTime*60):
#             self.progress.step()
#             init+=1
#             new_thread = threading.Thread(target=self.changeLabel)
#             new_thread.setDaemon(True)
#             new_thread.start()
#             time.sleep(1)
    
#     def changeLabel(self):
#         self.pP.set(str(((self.variable.get()/2700)*100)))
#         self.root.update()


# if __name__ == '__main__':
#     progress = ProgressBar()
#     progress.start()
