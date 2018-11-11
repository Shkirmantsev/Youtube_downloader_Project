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


class Missionbox(Frame):  # add non-modal form box

    def __init__(self, configs=None, box=None):

        configs = configs or self.configs_test # self.configs_test is down under

        missionboxframe=Frame(box, bd=2, relief=GROOVE)
        missionboxframe.grid(row=1, column=0,columnspan=2, sticky=NSEW)
        missionboxframe.columnconfigure(0, weight=1)

        # images for Buttons
        #imgpath = str(os.getcwd()) + "/hutro.png"
        #self.img = PhotoImage(file=imgpath)




#############   embeding buttons in box: start ####

        def embed(i, boxplace, text, func, imgstr=None, column=None,columnspan=None):
            def funccommand(self=self,func=func):
                # return func(self) #<- this solution will not work in GUI_Download_start
                return eval("self.{0}()".format(func.__name__))

            butt=Button(boxplace, text=text, command=funccommand)
            butt.grid(row=i, column=column or 0, columnspan=columnspan or 2, sticky=NSEW)
            boxplace.rowconfigure(i, weight=1)
            if imgstr:
                img=self.returnimage(imgstr)
                butt.config(image=img)


        lenconfig = len(configs)

        for i in range(lenconfig): embed(i, missionboxframe, configs[i][0], configs[i][1], configs[i][2])


############## end        ###############




    #return img path in class from images' name
    def returnimage(self, imgpng): return getattr(self, "{0}".format(imgpng))


######## functions Prototipes

    def onSubmit(self): print("onSubmit missionbox function proto. just not implemented")
    def onCancel(self): print("onCancel missionbox function proto. just not implemented")
    def onDwnldaudio(self): print("onDwnldaudio missionbox function proto. just not implemented")
    def onChoose(self): print("onChoose missionbox function proto. just not implemented")
    def onConvert(self): print("onConvert missionbox function proto. just not implemented")

########

    configs_test = (
        ('Download_video', onSubmit, None),
        ('Download_as_audio', onDwnldaudio, None),
        ('choose video for convert in audio', onChoose, None),
        ('start convert in audio', onConvert, None),
        ('Exit', onCancel, None),
                    )


if __name__ == '__main__':
    box = Frame(parent=None)  # box has rows, buttons
    box.pack(expand=YES, fill=BOTH)  # rows has row frames
    box.rowconfigure(0, weight=1)
    box.columnconfigure(0, weight=1)

    Missionbox(box=box)
    mainloop()