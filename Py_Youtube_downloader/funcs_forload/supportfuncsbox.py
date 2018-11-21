#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

import funcs_forload.pyperclip as pyperclip
from tkinter.messagebox import showerror, showinfo
import p_youtube_loader, os, sys, _thread
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from multiprocessing import Process, Lock
from funcs_forload.funcbox_forload import pull_urlinfo
from p_youtube_loader import tmp_dir as loadertmp_dir
import re
# paste from clipboadr
def onPaste(self):
    try:
        self.text = pyperclip.paste()
        pp = self.text
        print(pp)
    except TclError:
        showerror('Youtube Downloader', 'Nothing to paste into URL-field from Clipboard')
        return
    self.content['video_url for download:'].insert(0, str(self.text))
    try:
        self.content['Saving_directory'].delete(0, END)
        self.content['Saving_file_name'].delete(0, END)
        self.content['video_file_to_convert'].delete(0, END)
    except: print("can not clean fields from old information")



#start download process video
def transfer(self, video_url, directory=None, file_name=None, quality_mode=None, ):
    #lock marker declaration
    lock=self.lock
    try:
        self.do_transfer(video_url, directory, file_name, quality_mode)
        # print('saved in "%s"'  % (p_youtube_loader.tmp_dir))
    except:
        with lock:
            print('Download failed', end=' ')
        with lock:
            print(sys.exc_info()[0], sys.exc_info()[1])

        #self.mutex.release()


#start
def onSubmit(self):
    #Form.onSubmit(self)
    # Collect all data from fields of form (databox)
    video_url = self.content['video_url for download:'].get()
    print(video_url)
    quality_mode  = int(self.content['quality_mode or press enter'].get())
    print("choosed quality_mode is ", quality_mode)

    directory = self.content['Saving_directory'].get()
    if directory == '': directory = None
    else: directory = os.path.normpath(directory)

    file_name = self.content['Saving_file_name'].get()
    if file_name == '':
        file_name = None
    else:
        extension=".mp4"
        if file_name[-4:]!=extension:
            file_name = str(file_name).replace(".", "-")
            file_name += extension
            if self.content['video_file_to_convert'].get()!='':

                directory=None
                file_name=None
                try:
                    self.content['Saving_directory'].delete(0, END)
                    self.content['Saving_file_name'].delete(0, END)
                    self.content['video_file_to_convert'].delete(0, END)
                    directory = None
                    file_name = None
                except: print("can not clean wrong field")

        print("choosed file name is ", file_name)

    self.mutex.acquire()
    self.threads += 1
    self.mutex.release()
    ftpargs = (video_url, directory, file_name, quality_mode)
    _thread.start_new_thread(self.transfer, ftpargs)
    showinfo(self.title, 'download of "%s" started' % (file_name or p_youtube_loader.tmp_filename))


 #download at first video, then convert in audio. Via Process
def onDwnldaudio(self):

    #lock marker for process
    lock=self.lock


    #Form.onSubmit(self)
    # Collect all data from fields of form (databox)
    video_url = self.content['video_url for download:'].get()
    print(video_url)
    videotitel=pull_urlinfo(video_url)['title'][0]
    if videotitel[-4:]!=".mp4": videotitel=videotitel+".mp4"

    quality_mode  = int(self.content['quality_mode or press enter'].get())
    print("choosed quality_mode is ", quality_mode)

    directory = self.content['Saving_directory'].get()
    if directory == '': directory = None
    else: directory = os.path.normpath(directory)

    file_name = self.content['Saving_file_name'].get()
    if file_name == '':
        file_name = None
    else:
        extension=".mp4"
        if file_name[-4:]!=extension:
            file_name = str(file_name).replace(".", "-")
            file_name += extension
            if self.content['video_file_to_convert'].get()!='':

                directory=None
                file_name=None
                try:
                    self.content['Saving_directory'].delete(0, END)
                    self.content['Saving_file_name'].delete(0, END)
                    self.content['video_file_to_convert'].delete(0, END)
                    directory = None
                    file_name = None
                except: print("can not clean wrong field")

        print("choosed file name is ", file_name)

    #self.mutex.acquire()
    with lock:
        self.threads += 1
        print("increase processes: ",self.threads)
    #self.mutex.release()
    ftpargs = (video_url, directory, file_name, quality_mode)
    def tmpfunc(transfer=self.transfer,ftpargs=ftpargs):
        file_name=ftpargs[2]
        transferprocess=Process(target=transfer, args=ftpargs)

        transferprocess.start()
        showinfo(self.title, 'download of "%s" started' % (file_name or p_youtube_loader.tmp_filename))
        transferprocess.join()


        directory=ftpargs[1] or loadertmp_dir
        file_name=file_name or videotitel
        my_file_addr=directory+os.path.sep+file_name

        newaudio=my_file_addr
        if newaudio[-4:]==".mp4":
            newaudio=newaudio[:-4]+".mp3"
        else: newaudio=newaudio+".mp3"

        thr=self.threads
        print("will converted from: ",my_file_addr,"\n to: \n", newaudio)

        convertprprocess = Process(target=self.convertinmp3, args=(my_file_addr,newaudio,thr,lock))
        convertprprocess.start()
        convertprprocess.join()
        self.threads -= 1


    _thread.start_new_thread(tmpfunc, (self.transfer,ftpargs))




# exit from program
def onCancel(self):
    if self.threads == 0:
        print("Bye!!!")
        Tk().quit()
    else:
        showinfo(self.title,'Cannot exit: %d threads running' % self.threads)



def onSave(self):  # save as file dialog
    save_as_file = asksaveasfilename()
    directory = os.path.dirname(save_as_file)
    file_name = os.path.basename(save_as_file)
    self.content['Saving_directory'].delete(0, END)
    self.content['Saving_directory'].insert(0, str(directory))
    self.content['Saving_file_name'].delete(0, END)
    self.content['Saving_file_name'].insert(0, str(file_name))

# Choose with askopenfile the video file to convert in audio:
def onChoose(self):
    choose_as_file=askopenfilename()
    choose_as_file=os.path.normpath(choose_as_file)
    directory = os.path.dirname(choose_as_file)
    file_name = os.path.basename(choose_as_file)
    self.content['video_file_to_convert'].delete(0, END)
    self.content['video_file_to_convert'].insert(0, str(choose_as_file))
    try:
        self.content['Saving_directory'].delete(0, END)
        self.content['Saving_directory'].insert(0, str(directory))
        self.content['Saving_file_name'].delete(0, END)
        file_name=str(file_name)
        extension = ".mp3"
        file_name= file_name[:-4]+extension
        self.content['Saving_file_name'].insert(0, str(file_name))
    except: print("can not save mp3 file name")
    print('Saving_directory: ', self.content['video_file_to_convert'].get())
    print('Saving_directory: ', self.content['Saving_directory'].get())
    print('Saving_file_name: ', self.content['Saving_file_name'].get())


def onConvert(self):


    convfunc = self.convertinmp3
    thr = self.threads
    lock=self.lock
    try:
        videofrom = self.content['video_file_to_convert'].get()
        print('videofrom: ',videofrom)
        musicdir=self.content['Saving_directory'].get()
        print('musicdir: ', musicdir)
        musicname=self.content['Saving_file_name'].get()
        musicfullname=musicdir+os.path.sep+musicname
        musicfullname=str(os.path.normpath(musicfullname))
    except: print('can not pick data from fields to cnvert')

    Process(target=convfunc, args=(videofrom,musicfullname,thr,lock)).start()


def closing(self): self.quality_modes.grid_forget()

def update_button(self):
    print('TEST2')
    tmp=self.content['quality_mode or press enter'].get()
    if tmp.isdigit(): self.var.set(tmp)
    else:
        self.var.set(1)
        self.content['quality_mode or press enter'].delete(0, END)
        self.content['quality_mode or press enter'].insert(0, 1)

    self.quality_modes.grid(row=0, column=2, rowspan=2, sticky=NSEW)
    self.children=self.quality_modes.winfo_children()
    print('children: ',self.children)
    for child in self.children[1:]:
        child.destroy()
    for key in self.content_modes:
        Radiobutton(self.quality_modes, text=self.content_modes[key], command=self.onPress, variable=self.var, value=key).pack(
                anchor=NW)
    #self.var.set(1)

    def funccommand(self=self):
        # func(self) <- this solution will not work in GUI_Download_start
        return eval("self.closing()")

    buttclosing=Button(self.quality_modes, text="<<<", command=funccommand)
    buttclosing.pack()

    self.quality_modes.update()


def add_quality(self):
    video_url = self.content['video_url for download:'].get()
    self.content_modes=p_youtube_loader.analise(video_url)
    content_modes=self.content_modes
    print(content_modes)
    self.update_button()





def onPress(self):
    pick=self.var.get()
    #print('you pressed ', pick)
    #print('result',self.content_modes[pick])
    self.content['quality_mode or press enter'].delete(0, END)
    self.content['quality_mode or press enter'].insert(0, pick)









