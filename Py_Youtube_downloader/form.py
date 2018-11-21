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
from forms_parts.missionbox import Missionbox

class Form(Databox,Buttonbox,Missionbox):                                           # add non-modal form box
    def __init__(self, labels, parent=None):          # pass field labels list


        box = Frame(parent)                             # box has rows, buttons
        box.pack(expand=YES, fill=BOTH)                   # rows has row frames
        box.rowconfigure(0, weight=1)
        box.columnconfigure(0, weight=1)


        Databox.__init__(self,labels,entrsize=80, box=box)
        Buttonbox.__init__(self, self.configs, box=box)
        Missionbox.__init__(self,self.configsmission, box=box)

        print("running child Class: ", self.__class__.__name__)

        ######Additive advertising block start : =>>

        partner = Label(box, text="Our Partners:")
        partner.grid(row=2, columnspan=2, sticky=NSEW)

        # images for Buttons
        imgpath = str(os.getcwd()) + "/hutro.png"
        self.img = PhotoImage(file=imgpath)

        but = Button(box, command=self.opensite)
        but.grid(row=3, column=0, columnspan=2, sticky=NSEW)
        but.config(image=self.img)

        # Additive advertising block end <<==     ###########

        box.master.bind('<Return>', (lambda event: self.onSubmit()))



        """def create_quality_modes(self):
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
            self.quality_modes.grid_forget()"""

        self.create_quality_modes(box)
        #children=self.quality_modes.winfo_children()
        #print('children: ',children)
        #children[1].destroy()

    def create_quality_modes(self,box):
        self.quality_modes = Frame(box, bd=2, relief=GROOVE)  # go=button or return key

        self.quality_modes.grid(row=0, column=2, sticky=NSEW)
        Label(self.quality_modes, text="quality modes:").pack(anchor=NW, expand=NO)

        self.content_modes = {1: 'test1'}
        self.var = IntVar()
        for key in self.content_modes:
            Radiobutton(self.quality_modes, text=self.content_modes[key], command=self.onPress, variable=self.var,
                        value=key).pack(
                anchor=NW, )

        self.var.set(1)
        self.quality_modes.grid_forget()

    def onSubmit(self):                                      # override this
        print(self.__class__.__name__)
        for key in self.content:                             # user inputs in
            print(key, '\t=>\t', self.content[key].get())    # self.content[k]

    def onCancel(self):                                      # override if need
        print(self.__class__.__name__)
        Tk().quit()                                          # default is exit

    #Prototipes
    def closing(self): print("closing quality function proto in 'form'. just not implemented")
    def onSave(self): print("save_as_file function proto in 'form'. just not implemented") # save as file dialog
    def add_quality(self): print("quality function proto in 'form'. just not implemented")
    def onPaste(self):
        print(self.__class__.__name__)
        print("onPaste function proto in 'form'. just not implemented")
    def onDwnldaudio(self): print("onDwnldaudio function proto in 'form'. just not implemented")
    def onChoose(self): print("onChoose function proto in 'form'. just not implemented")
    def onConvert(self): print("onConvert function proto in 'form'. just not implemented")

    def onPress(self):
        pick=self.var.get()
        print('you pressed ', pick)
        print('result',self.content_modes[pick])

    def update_button(self): print("update_button function proto in 'form'. just not implemented")


    def opensite(self): open_site('http://hutro-meh.com')

    configs = (("Paste URL", onPaste),
               ('add_quality', add_quality),
               ('Save as', onSave))

    # Name, func, name of png image, "column if not 0 or None", columnspan or None
    configsmission = (
        ('Download_video', onSubmit, None),
        ('Download_as_audio', onDwnldaudio, None),
        ('choose video for convert in audio', onChoose, None),
        ('start convert in audio', onConvert, None),
        ('Exit', onCancel, None),
                    )



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
