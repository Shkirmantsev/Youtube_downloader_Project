#!/usr/bin/pypy3
# -*- coding: utf-8 -*-


"""
  Class Databox that is creating box with entry data for Form
for example
 Name: textfield
 Age: textfield
 job: textfield
"""

from tkinter import *
from tkinter.messagebox import showinfo

class Databox(Frame):                                           # add non-modal form box
    def __init__(self, labels,entrsize=80, box=None):          # pass field labels list


        labelsize = max(len(x) for x in labels) + 2

        rows = Frame(box, bd=2, relief=GROOVE)        # go=button or return key
        rows.grid(row=0, column=0, sticky=NSEW)       # runs onSubmit method
        rows.columnconfigure(1,weight=1)


        self.content = {}
        i=0
        for label in labels:

            row = Label(rows, text=label, width=labelsize)
            row.grid(row=i, column=0, sticky=NSEW)
            rows.rowconfigure(i, weight=1)

            entry = Entry(rows, relief=SUNKEN, width=entrsize)
            entry.grid(row=i, column=1, sticky=NSEW )



            try:
                self.content[label] = entry
            except:
                entrysize=entrysize*2
                entry = Entry(row, width=entrsize)
                entry.grid(row=i, column=1, sticky=NSEW)
                self.content[label] = entry
            i += 1

        box.master.bind('<Return>', (lambda event: self.onSubmit()))

        

    def onSubmit(self):                                      # override this
        for key in self.content:                             # user inputs in
            print(key, '\t fromdatabox =>\t', self.content[key].get())    # self.content[k]

        return  self.content



if __name__ == '__main__':
    box = Frame(parent=None)  # box has rows, buttons
    box.pack(expand=YES, fill=BOTH)  # rows has row frames
    box.rowconfigure(0, weight=1)
    box.columnconfigure(0, weight=1)

    Databox(['Name', 'Age', 'Job'],box=box)
    mainloop()



