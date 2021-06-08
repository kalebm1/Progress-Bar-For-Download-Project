#@author: Kaleb Morgan
#@useCase: Sending download via WiFi to keep user informed
#of the happening of their PC.
from tkinter import *
from tkinter.ttk import *
import time

#Time you want the progress bar to run for (in minutes)
progressBarTime = 45
#Title of the window
title = "Download"
#TKinter object
root = Tk()
#Setting the title to the title variable mentioned above
root.title( title)
#Setting the icon in the top right of the screen(must be .ico file type)
root.iconbitmap(r'E:\code projects\Progress Bar\SRAppIconWBG.ico')
#Checks if the bar has already ran or not(prevent looping)
ran = False
#String variable to keep label words in one variable(helps us change the message when the progress bar is finished)
textr = StringVar()
#Adding a label with text = String variable above
label = Label(root,textvariable=textr)
#Setting the value of the String var to what we want the label to say.
textr.set("Downloading...")
#Double variable to keep track of bar progress(would have to use threading to get to work)
var1 = DoubleVar(root)
#Making the progress bar object with max value the progress time in seconds
progress = Progressbar(root, orient = HORIZONTAL, length = 600, mode = 'determinate',maximum=(progressBarTime*60),variable=var1)
#Adding padding to the label
label.pack(pady=(30,0))
#Adding padding to the progress bar
progress.pack(padx = 30,pady=(10,40))

#Method to start the progress bar counting at 1 step per second.
def bar():
    progress.start(1000)

#Method to show the new message once progress bar is completed
def newMessage():
    #Stop the progress bar
    progress.stop()
    #Set the label var = new message
    textr.set("Download Complete!")
    #Make a button for the user to close the window easily
    button = Button(root,text="Close Window",command=doTheQuit)
    #Add padding to the button
    button.pack(pady=(0,25))

#Method to quit the program
def doTheQuit():
    root.quit()

  
#Initialize the progress bar
if(var1.get()<=100):
    bar()
ran = True

#Wait one second before the amount of time is up to display new
#message and stop the progress bar. This prevents the overall
#progress bar from looping endlessly once it reaches the end.
root.after(int((progressBarTime*60-1)*1000),newMessage)
  
# infinite loop
mainloop()