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
from forms_parts.buttonbox import Buttonbox


class Form:                                           # add non-modal form box
    def __init__(self, labels, parent=None):          # pass field labels list

        box = Frame(parent)                             # box has rows, buttons
        box.pack(expand=YES, fill=BOTH)                   # rows has row frames
        box.rowconfigure(0, weight=1)
        box.columnconfigure(0, weight=1)

        databox=Databox(labels,entrsize=80, box=box)
        self.content=databox.content

        #create buttons menu: save_as,past url,... actr
        buttonbox=Buttonbox(self.configs, box=box)


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

    #Prototipes
    def onSave(self): print("save_as_file function proto in 'form'. just not implemented") # save as file dialog
    def add_quality(self): print("quality function proto in 'form'. just not implemented")
    def onPaste(self): print("onPaste function proto in 'form'. just not implemented")

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

    def opensite(self): open_site('http://hutro-meh.com')

    configs = (("Paste URL", onPaste),
               ('add_quality', add_quality),
               ('Save as', onSave))



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
