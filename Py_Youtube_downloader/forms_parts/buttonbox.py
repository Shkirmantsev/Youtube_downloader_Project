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
from .embedfactory import Embedfac

class Buttonbox(Embedfac):  # add non-modal form box

    def __init__(self, configs=None, box=None):

        configs = configs or self.configs_test # self.configs_test is down under

        dialogs = Frame(box, bd=2, relief=GROOVE)  # go=button or return key
        dialogs.grid(row=0, column=1, sticky=NSEW)
        dialogs.rowconfigure(0, weight=1)

        #############   embeding buttons in box: start ####


        lenconfig = len(configs)

        for i in range(lenconfig): self.embed(i, dialogs, configs[i][0], configs[i][1])

        ############## end        ###############


######## functions Prototipes

    def onPaste(self): print("onPaste function proto. just not implemented")
    def onSave(self): print("onSave function proto. just not implemented")
    def add_quality(self): print("add_quality function proto. just not implemented")
########

    configs_test = (("Paste URL", onPaste),
                    ('add_quality', add_quality),
                    ('Save as', onSave))


if __name__ == '__main__':
    box = Frame(parent=None)  # box has rows, buttons
    box.pack(expand=YES, fill=BOTH)  # rows has row frames
    box.rowconfigure(0, weight=1)
    box.columnconfigure(0, weight=1)

    Buttonbox(box=box)
    mainloop()
