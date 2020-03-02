import sys
import os
import subprocess
from tkinter import *

r = Tk()
r.geometry('800x600')
r.title('EMOvie')
r.configure(bg='black')
def callBack():
    cmd = 'python movie.py'
    output=subprocess.check_output(cmd, shell=True)
    l3['text']=output.strip()
    
class StdoutRedirector(object):

    def __init__(self):
        self.result = ''

    def write(self, text):
        self.result += text

l1=Label(r,text='Movie Recomendation' , font=('Helvetica,  50'), fg='#ff7000', bg='Black')
l2=Label(r,text='using Emotional Recognition' , font=('Helvetica,  20'), fg='White', bg='Black')
l3=Label(r,text='' , font=('Helvetica,  30'), fg='#c300e4', bg='Black')
button1= Button(r,text='START', command=callBack, font=('Helvetica, 36'),bg='#ff7000', fg='Black')

l1.pack()
l2.pack()
button1.pack()
l3.pack()
r.mainloop()
