#!/usr/bin/pypy3
# -*- coding: utf-8 -*-


"""
  Class Buttonbox that is creating box with Functions Button for Form
for example
 [Paste URL] => onPaste()
  [Save as] => onSave()
  [add_qualit] => add_qualit ()

"""

from tkinter import *
import os


class Embedfac(Frame):  # add non-modal form box

    def __init__(self, configs=None, box=None):


        configs = configs or self.configs_test # self.configs_test is down under

        boxframe=Frame(box, bd=2, relief=GROOVE)
        boxframe.grid(row=1, column=0,columnspan=2, sticky=NSEW)
        boxframe.columnconfigure(0, weight=1)

        # images for Buttons
        imgpath = str(os.getcwd()) + "/exit.png"
        self.testimg = PhotoImage(file=imgpath)

        lenconfig = len(configs)

        for i in range(lenconfig): self.embed(i, boxframe, configs[i][0], configs[i][1], configs[i][2])




#############   embeding buttons in box: start ####

    def embed(self,i, boxplace, text, func, imgstr=None, column=None,columnspan=None):
        def funccommand(self=self,func=func):
            # return func(self) #<- this solution will not work in GUI_Download_start
            return eval("self.{0}()".format(func.__name__))

        butt=Button(boxplace, text=text, command=funccommand)
        butt.grid(row=i, column=column or 0, columnspan=columnspan or 2, sticky=NSEW)
        boxplace.rowconfigure(i, weight=1)
        if imgstr:
            img=self.returnimage(imgstr)
            butt.config(image=img)

############## end        ###############


    #return img path in class from images' name
    def returnimage(self, imgpng): return getattr(self, "{0}".format(imgpng))


######## functions Prototipes

    def onCancel(self): print("onCancel missionbox function proto. just not implemented")

########

    configs_test = (('Exit', onCancel, 'testimg'),)


if __name__ == '__main__':
    box = Frame(parent=None)  # box has rows, buttons
    box.pack(expand=YES, fill=BOTH)  # rows has row frames
    box.rowconfigure(0, weight=1)
    box.columnconfigure(0, weight=1)

    Embedfac(box=box)
    mainloop()