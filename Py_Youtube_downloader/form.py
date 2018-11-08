"""
##################################################################
basic form class for GUI. Used by Shkirmantsev
##################################################################
"""

from tkinter import *
from tkinter.filedialog import asksaveasfilename
from webbrowser import open as open_site
import os
from forms_parts.databox import Databox


class Form:                                           # add non-modal form box
    def __init__(self, labels,entrsize=80, parent=None):          # pass field labels list

        box = Frame(parent)                             # box has rows, buttons
        box.pack(expand=YES, fill=BOTH)                   # rows has row frames
        box.rowconfigure(0, weight=1)
        box.columnconfigure(0, weight=1)

        databox=Databox(labels, box=box)
        self.content=databox.content


        dialogs = Frame(box, bd=2, relief=GROOVE)  # go=button or return key
        dialogs.grid(row=0, column=1, sticky=NSEW)
        dialogs.rowconfigure(0, weight=1)



        paste_button = Button(dialogs, text='Paste URL', command=self.onPaste)
        paste_button.grid(row=0, column=0, sticky=NSEW)
        dialogs.rowconfigure(0, weight=1)

        b = Button(dialogs, text='Save as', command=self.onSave)
        b.grid(row=2, column=0, sticky=NSEW)
        dialogs.rowconfigure(2, weight=0)

        quality_button=Button(dialogs, text='add_quality', command=self.add_quality)
        quality_button.grid(row=1, column=0, sticky=NSEW)
        dialogs.rowconfigure(1, weight=1)

        dwnld_button=Button(box, text='Download', command=self.onSubmit)
        dwnld_button.grid(row=1, column=0,sticky=NSEW)
        Button(box, text='Exit', command=self.onCancel).grid(row=1, column=1, sticky=NSEW)

        partner = Label(box, text="Our Partners:")
        partner.grid(row=2, columnspan=2, sticky=NSEW)
        a=str(os.getcwd())+"/hutro.png"
        self.img=PhotoImage(file=a)

        but=Button(box, command=self.opensite)
        but.grid(row=3, column=0, columnspan=2, sticky=NSEW)
        but.config(image=self.img)


        box.master.bind('<Return>', (lambda event: self.onSubmit()))

        def create_quality_modes(self):
            self.quality_modes = Frame(box, bd=2, relief=GROOVE)  # go=button or return key

            self.quality_modes.grid(row=0, column=2, sticky=NSEW)
            Label(self.quality_modes, text="quality modes:").pack(anchor=NW, expand=NO)

            self.content_modes = {1:'test1'}
            self.var = IntVar()
            for key in self.content_modes:
                Radiobutton(self.quality_modes, text=self.content_modes[key], command=self.onPress, variable=self.var,
                            value=key).pack(
                    anchor=NW, )


            self.var.set(1)

            self.quality_modes.grid_forget()
        create_quality_modes(self)
        #children=self.quality_modes.winfo_children()
        #print('children: ',children)
        #children[1].destroy()



    def onSubmit(self):                                      # override this
        for key in self.content:                             # user inputs in
            print(key, '\t=>\t', self.content[key].get())    # self.content[k]

    def onCancel(self):                                      # override if need
        Tk().quit()                                          # default is exit

    def onSave(self):                                      # save as file dialog
        pass
        save_as_file=asksaveasfilename()
        print(save_as_file)

        return save_as_file

    def add_quality(self): print("quality")

    def onPaste(self): pass

    def onPress(self):
        pick=self.var.get()
        print('you pressed ', pick)
        print('result',self.content_modes[pick])

    def update_button(self):
        print('TEST2')

        self.quality_modes.grid(row=0, column=2, sticky=NSEW)
        self.children=self.quality_modes.winfo_children()
        print('children: ',self.children)

        for child in self.children[1:]:
            child.destroy()


        for key in self.content_modes:
            Radiobutton(self.quality_modes, text=self.content_modes[key], command=self.onPress, variable=self.var, value=key).pack(
                anchor=NW)
        self.var.set(1)
        self.quality_modes.update()

    def opensite(self):

        open_site('http://hutro-meh.com')




class DynamicForm(Form):
    def __init__(self, labels=None):
        labels = input('Enter field names: ').split()
        Form.__init__(self, labels)
    def onSubmit(self):
        print('Field values...')
        Form.onSubmit(self)
        self.onCancel()

if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        Form(['lable_Name', 'lable_Age', 'Lable_Job'])     # precoded fields, stay after submit
    else:
        DynamicForm()                    # input fields, go away after submit
    mainloop()
