import tkinter as tk
import threading
import time
import sys


class myapps:
    def __init__(self,root:tk.Tk,startsubs,mainsubs,titles:str,backgrounds:str,foregrounds:str):
        self.root=root
        self.root.title(titles)
        self.root.configure(background=backgrounds)
        self.fogrounds=foregrounds
        self.startsubs=startsubs
        self.mainsubs=mainsubs
        self.time=threading.Thread(target=self.mains)
        
        self.startsubs(self,self.root)
        
        self.time.start()
    def mains(self):
        self.mainsubs(self,self.root)
        
        





def inits(startsubs,mainsubs,title:str,backgrounds:str,foregrounds:str):
    root=tk.Tk()
    apps=myapps(root,startsubs,mainsubs,title,backgrounds,foregrounds)
    root.mainloop()
    exit()


global outs
outs=False

def mainloop(selfs,root:tk.Tk):
    count=0
    while not(outs):
        print(count)
        try:
           selfs.text.delete("0","end")
           selfs.text.insert("0",str(count))
        except:
           break
        time.sleep(1)
        count=count+1



def startmain(selfs,root:tk.Tk):
    selfs.text=tk.Entry(background="black",foreground="white")
    selfs.text.pack(padx=10,pady=10)
   



apps=inits(startsubs=startmain,mainsubs=mainloop,title="my apps",backgrounds="black", foregrounds="white")
outs=True
time.sleep(3)